window.testdata = function () {

    var elementsById = {};
    var LEVEL = {I:'info', H:'info', T:'trace', W:'warn', E:'error', D:'debug', F:'fail'};
    var KEYWORD_TYPE = {kw: 'KEYWORD',
        setup:'SETUP',
        teardown:'TEARDOWN',
        forloop:'FOR',
        foritem:'VAR'
    };
    var _statistics = null;

    function get(id) {
        return store.get(id)
    }

    function addElement(elem) {
        elem.id = uuid();
        elementsById[elem.id] = elem;
        return elem;
    }

    var idCounter=0;

    // TODO: Rename this function. 
    function uuid() {
        idCounter++;
        return "elementId_"+idCounter;
    }

    function timestamp(millis) {
        return new Date(window.output.baseMillis + millis);
    }

    function times(stats) {
        var startMillis = get(stats[1]);
        var elapsed = get(stats[2]);
        if(startMillis == null){
            return [null, null, elapsed];
        }
        return [timestamp(startMillis), timestamp(startMillis + elapsed), elapsed];
    }

    function message(element) {
        return addElement(model.Message(LEVEL[get(element[1])], timestamp(get(element[0])),
                                        get(element[2]), get(element[3])));
    }

    function parseStatus(stats, parentSuiteTeardownFailed) {
        if (parentSuiteTeardownFailed)
            return model.FAIL;
        return {'P': model.PASS, 'F': model.FAIL, 'N': model.NOT_RUN}[get(stats[0])];
    }

    function last(items) {
        return items[items.length-1];
    }

    function secondLast(items) {
        return items[items.length-2];
    }

    function childCreator(parent, childType) {
        return function (elem, index) {
            return addElement(childType(parent, elem, index));
        };
    }

    function createKeyword(parent, element, index) {
        var kw = model.Keyword({
            type: KEYWORD_TYPE[get(element[0])],
            name: get(element[1]),
            args: get(element[4]),
            doc: get(element[3]),
            status: parseStatus(last(element)),
            times: model.Times(times(last(element))),
            parent: parent,
            index: index
        });
        kw.populateKeywords(Populator(element, keywordMatcher, childCreator(kw, createKeyword)));
        kw.populateMessages(Populator(element, messageMatcher, message));
        return kw;
    }

    var keywordMatcher = headerMatcher("kw", "setup", "teardown", "foritem", "forloop");

    function messageMatcher(elem) {
        return (elem.length == 3 &&
                typeof(get(elem[0])) == "number" &&
                typeof(get(elem[1])) == "string" &&
                typeof(get(elem[2])) == "string");
    }

    function tags(taglist) {
        return util.map(taglist, get);
    }

    function createTest(suite, element) {
        var statusElement = last(element);
        var test = model.Test({
            parent: suite,
            name: get(element[1]),
            doc: get(element[4]),
            timeout: get(element[2]),
            isCritical: (get(element[3]) == "Y"),
            status: parseStatus(statusElement, suite.hasTeardownFailure()),
            message: createMessage(statusElement, suite.hasTeardownFailure()),
            times: model.Times(times(statusElement)),
            tags: tags(secondLast(element))
        });
        test.populateKeywords(Populator(element, keywordMatcher, childCreator(test, createKeyword)));
        return test;
    }

    function createMessage(statusElement, hasSuiteTeardownFailed) {
        var message = statusElement.length == 4 ? get(statusElement[3]) : '';
        if (!hasSuiteTeardownFailed)
            return message;
        if (message)
            return message + '\n\nAlso teardown of the parent suite failed.';
        return 'Teardown of the parent suite failed.';
    }

    function createSuite(parent, element) {
        var statusElement = secondLast(element);
        var suite = model.Suite({
            parent: parent,
            name: get(element[2]),
            source: get(element[1]),
            doc: get(element[3]),
            status: parseStatus(statusElement, parent && parent.hasTeardownFailure()),
            parentSuiteTeardownFailed: parent && parent.hasTeardownFailure(),
            message: createMessage(statusElement, parent && parent.hasTeardownFailure()),
            times: model.Times(times(statusElement)),
            statistics: suiteStats(last(element)),
            metadata: parseMetadata(element[4])
        });
        suite.populateKeywords(Populator(element, keywordMatcher, childCreator(suite, createKeyword)));
        suite.populateTests(Populator(element, headerMatcher("test"), childCreator(suite, createTest)));
        suite.populateSuites(Populator(element, headerMatcher("suite"), childCreator(suite, createSuite)));
        return suite;
    }

    function parseMetadata(data) {
        var metadata = [];
        for (var i=0; i<data.length; i+=2) {
            metadata.push([get(data[i]), get(data[i+1])]);
        }
        return metadata;
    }

    function suiteStats(stats) {
        stats = util.map(stats, get);
        return {
            total: stats[0],
            totalPassed: stats[1],
            totalFailed: stats[0] - stats[1],
            critical: stats[2],
            criticalPassed: stats[3],
            criticalFailed: stats[2] - stats[3]
        };
    }

    function headerMatcher() {
        var args = arguments;
        return function(elem) {
            for (var i = 0; i < args.length; i++)
                if (get(elem[0]) == args[i]) return true;
            return false;
        };
    }

    function Populator(element, matcher, creator) {
        var items = findElements(element, matcher);
        return {
            numberOfItems: items.length,
            creator: function (index) {
                return creator(items[index], index);
            }
        };
    }

    function findElements(fromElement, matcher) {
        var results = new Array();
        for (var i = 0; i < fromElement.length; i++)
            if (matcher(fromElement[i]))
                results.push(fromElement[i]);
        return results;
    }

    function suite() {
        var elem = window.output.suite;
        if (elementsById[elem.id])
            return elem;
        var main = addElement(createSuite(undefined, elem));
        window.output.suite = main;
        return main;
    }

    function findById(id) {
        return elementsById[id];
    }

    function pathToKeyword(fullName) {
        var root = suite();
        if (fullName.indexOf(root.fullName + ".") != 0) return [];
        return keywordPathTo(fullName + ".", root, [root.id]);
    }

    function pathToTest(fullName) {
        var root = suite();
        if (fullName.indexOf(root.fullName + ".") != 0) return [];
        return testPathTo(fullName, root, [root.id]);
    }

    function pathToSuite(fullName) {
        var root = suite();
        if (fullName.indexOf(root.fullName) != 0) return [];
        if (fullName == root.fullName) return [root.id];
        return suitePathTo(fullName, root, [root.id]);
    }

    function keywordPathTo(fullName, current, result) {
        if (fullName == "") return result;
        for (var i = 0; i < current.numberOfKeywords; i++) {
            var kw = current.keyword(i);
            if (fullName.indexOf(kw.path + ".") == 0) {
                result.push(kw.id);
                if (fullName == kw.path + ".")
                    return result;
                return keywordPathTo(fullName, kw, result);
            }
        }
        for (var i = 0; i < current.numberOfTests; i++) {
            var test = current.test(i);
            if (fullName.indexOf(test.fullName + ".") == 0) {
                result.push(test.id);
                return keywordPathTo(fullName, test, result);
            }
        }
        for (var i = 0; i < current.numberOfSuites; i++) {
            var suite = current.suite(i);
            if (fullName.indexOf(suite.fullName + ".") == 0) {
                result.push(suite.id);
                return keywordPathTo(fullName, suite, result);
            }
        }
    }

    function testPathTo(fullName, currentSuite, result) {
        for (var i = 0; i < currentSuite.numberOfTests; i++) {
            var test = currentSuite.test(i);
            if (fullName == test.fullName) {
                result.push(test.id);
                return result;
            }
        }
        for (var i = 0; i < currentSuite.numberOfSuites; i++) {
            var suite = currentSuite.suite(i);
            if (fullName.indexOf(suite.fullName + ".") == 0) {
                result.push(suite.id);
                return testPathTo(fullName, suite, result);
            }
        }
    }

    function suitePathTo(fullName, currentSuite, result) {
        for (var i = 0; i < currentSuite.numberOfSuites; i++) {
            var suite = currentSuite.suite(i);
            if (fullName == suite.fullName) {
                result.push(suite.id);
                return result;
            }
            if (fullName.indexOf(suite.fullName + ".") == 0) {
                result.push(suite.id);
                return suitePathTo(fullName, suite, result);
            }
        }
    }

    function generated() {
        return timestamp(window.output.generatedMillis);
    }

    function errors() {
        return util.map(window.output.errors, message);
    }

    function statistics() {
        if (!_statistics) {
            var statData = window.output.stats;
            _statistics = stats.Statistics(statData[0], statData[1], statData[2]);
        }
        return _statistics
    }

    return {
        suite: suite,
        errors: errors,
        find: findById,
        pathToTest: pathToTest,
        pathToSuite: pathToSuite,
        pathToKeyword: pathToKeyword,
        generated: generated,
        statistics: statistics
    };

}();

window.store = (function () {

    function getText(id) {
        var text = window.output.strings[id];
        if (text[0] == '*') {
            return text.substring(1)
        }
        var extracted = extract(text);
        window.output.strings[id] = "*"+extracted;
        return extracted;
    }

    function extract(text) {
        var decoded = JXG.Util.Base64.decodeAsArray(text);
        var extracted = (new JXG.Util.Unzip(decoded)).unzip()[0][0];
        return JXG.Util.utf8Decode(extracted);
    }

    function getInteger(id) {
        return window.output.integers[id];
    }

    function dispatch(id) {
        if (id == undefined) return undefined;
        if (id == null) return null;
        return id < 0 ? getInteger(-1 - id) : getText(id);
    }

    return {
        get: function (id) { return dispatch(id); }
    };

})();
