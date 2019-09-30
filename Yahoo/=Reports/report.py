<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Test Report</title>
    <link href="assets/style.css" rel="stylesheet" type="text/css"/></head>
  <body onLoad="init()">
    <script>/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */


function toArray(iter) {
    if (iter === null) {
        return null;
    }
    return Array.prototype.slice.call(iter);
}

function find(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return elem.querySelector(selector);
}

function find_all(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return toArray(elem.querySelectorAll(selector));
}

function sort_column(elem) {
    toggle_sort_states(elem);
    var colIndex = toArray(elem.parentNode.childNodes).indexOf(elem);
    var key;
    if (elem.classList.contains('numeric')) {
        key = key_num;
    } else if (elem.classList.contains('result')) {
        key = key_result;
    } else {
        key = key_alpha;
    }
    sort_table(elem, key(colIndex));
}

function show_all_extras() {
    find_all('.col-result').forEach(show_extras);
}

function hide_all_extras() {
    find_all('.col-result').forEach(hide_extras);
}

function show_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.remove("collapsed");
    expandcollapse.classList.remove("expander");
    expandcollapse.classList.add("collapser");
}

function hide_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.add("collapsed");
    expandcollapse.classList.remove("collapser");
    expandcollapse.classList.add("expander");
}

function show_filters() {
    var filter_items = document.getElementsByClassName('filter');
    for (var i = 0; i < filter_items.length; i++)
        filter_items[i].hidden = false;
}

function add_collapse() {
    // Add links for show/hide all
    var resulttable = find('table#results-table');
    var showhideall = document.createElement("p");
    showhideall.innerHTML = '<a href="javascript:show_all_extras()">Show all details</a> / ' +
                            '<a href="javascript:hide_all_extras()">Hide all details</a>';
    resulttable.parentElement.insertBefore(showhideall, resulttable);

    // Add show/hide link to each result
    find_all('.col-result').forEach(function(elem) {
        var collapsed = get_query_parameter('collapsed') || 'Passed';
        var extras = elem.parentNode.nextElementSibling;
        var expandcollapse = document.createElement("span");
        if (collapsed.includes(elem.innerHTML)) {
            extras.classList.add("collapsed");
            expandcollapse.classList.add("expander");
        } else {
            expandcollapse.classList.add("collapser");
        }
        elem.appendChild(expandcollapse);

        elem.addEventListener("click", function(event) {
            if (event.currentTarget.parentNode.nextElementSibling.classList.contains("collapsed")) {
                show_extras(event.currentTarget);
            } else {
                hide_extras(event.currentTarget);
            }
        });
    })
}

function get_query_parameter(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

function init () {
    reset_sort_headers();

    add_collapse();

    show_filters();

    toggle_sort_states(find('.initial-sort'));

    find_all('.sortable').forEach(function(elem) {
        elem.addEventListener("click",
                              function(event) {
                                  sort_column(elem);
                              }, false)
    });

};

function sort_table(clicked, key_func) {
    var rows = find_all('.results-table-row');
    var reversed = !clicked.classList.contains('asc');
    var sorted_rows = sort(rows, key_func, reversed);
    /* Whole table is removed here because browsers acts much slower
     * when appending existing elements.
     */
    var thead = document.getElementById("results-table-head");
    document.getElementById('results-table').remove();
    var parent = document.createElement("table");
    parent.id = "results-table";
    parent.appendChild(thead);
    sorted_rows.forEach(function(elem) {
        parent.appendChild(elem);
    });
    document.getElementsByTagName("BODY")[0].appendChild(parent);
}

function sort(items, key_func, reversed) {
    var sort_array = items.map(function(item, i) {
        return [key_func(item), i];
    });
    var multiplier = reversed ? -1 : 1;

    sort_array.sort(function(a, b) {
        var key_a = a[0];
        var key_b = b[0];
        return multiplier * (key_a >= key_b ? 1 : -1);
    });

    return sort_array.map(function(item) {
        var index = item[1];
        return items[index];
    });
}

function key_alpha(col_index) {
    return function(elem) {
        return elem.childNodes[1].childNodes[col_index].firstChild.data.toLowerCase();
    };
}

function key_num(col_index) {
    return function(elem) {
        return parseFloat(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function key_result(col_index) {
    return function(elem) {
        var strings = ['Error', 'Failed', 'Rerun', 'XFailed', 'XPassed',
                       'Skipped', 'Passed'];
        return strings.indexOf(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function reset_sort_headers() {
    find_all('.sort-icon').forEach(function(elem) {
        elem.parentNode.removeChild(elem);
    });
    find_all('.sortable').forEach(function(elem) {
        var icon = document.createElement("div");
        icon.className = "sort-icon";
        icon.textContent = "vvv";
        elem.insertBefore(icon, elem.firstChild);
        elem.classList.remove("desc", "active");
        elem.classList.add("asc", "inactive");
    });
}

function toggle_sort_states(elem) {
    //if active, toggle between asc and desc
    if (elem.classList.contains('active')) {
        elem.classList.toggle('asc');
        elem.classList.toggle('desc');
    }

    //if inactive, reset all other functions and add ascending active
    if (elem.classList.contains('inactive')) {
        reset_sort_headers();
        elem.classList.remove('inactive');
        elem.classList.add('active');
    }
}

function is_all_rows_hidden(value) {
  return value.hidden == false;
}

function filter_table(elem) {
    var outcome_att = "data-test-result";
    var outcome = elem.getAttribute(outcome_att);
    class_outcome = outcome + " results-table-row";
    var outcome_rows = document.getElementsByClassName(class_outcome);

    for(var i = 0; i < outcome_rows.length; i++){
        outcome_rows[i].hidden = !elem.checked;
    }

    var rows = find_all('.results-table-row').filter(is_all_rows_hidden);
    var all_rows_hidden = rows.length == 0 ? true : false;
    var not_found_message = document.getElementById("not-found-message");
    not_found_message.hidden = !all_rows_hidden;
}
</script>
    <h1>report.py</h1>
    <p>Report generated on 09-Sep-2019 at 13:23:06 by <a href="https://pypi.python.org/pypi/pytest-html">pytest-html</a> v1.20.0</p>
    <h2>Environment</h2>
    <table id="environment">
      <tr>
        <td>Packages</td>
        <td>{&apos;pytest&apos;: &apos;4.3.0&apos;, &apos;py&apos;: &apos;1.8.0&apos;, &apos;pluggy&apos;: &apos;0.9.0&apos;}</td></tr>
      <tr>
        <td>Platform</td>
        <td>Darwin-18.7.0-x86_64-i386-64bit</td></tr>
      <tr>
        <td>Plugins</td>
        <td>{&apos;xdist&apos;: &apos;1.26.1&apos;, &apos;metadata&apos;: &apos;1.8.0&apos;, &apos;html&apos;: &apos;1.20.0&apos;, &apos;forked&apos;: &apos;1.0.2&apos;, &apos;allure-pytest&apos;: &apos;2.6.1&apos;}</td></tr>
      <tr>
        <td>Python</td>
        <td>3.7.1</td></tr></table>
    <h2>Summary</h2>
    <p>1 tests ran in 5.58 seconds. </p>
    <p class="filter" hidden="true">(Un)check the boxes to filter the results.</p><input checked="true" class="filter" data-test-result="passed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="passed">0 passed</span>, <input checked="true" class="filter" data-test-result="skipped" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="skipped">0 skipped</span>, <input checked="true" class="filter" data-test-result="failed" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="failed">1 failed</span>, <input checked="true" class="filter" data-test-result="error" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="error">0 errors</span>, <input checked="true" class="filter" data-test-result="xfailed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xfailed">0 expected failures</span>, <input checked="true" class="filter" data-test-result="xpassed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xpassed">0 unexpected passes</span>
    <h2>Results</h2>
    <table id="results-table">
      <thead id="results-table-head">
        <tr>
          <th class="sortable result initial-sort" col="result">Result</th>
          <th class="sortable" col="name">Test</th>
          <th class="sortable numeric" col="duration">Duration</th>
          <th>Links</th></tr>
        <tr hidden="true" id="not-found-message">
          <th colspan="4">No results found. Try to check the filters</th></tr></thead>
      <tbody class="failed results-table-row">
        <tr>
          <td class="col-result">Failed</td>
          <td class="col-name">Test/test_login.py::TestLogin::test_login</td>
          <td class="col-duration">0.02</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log">self = &lt;test_login.TestLogin object at 0x1062359b0&gt;<br/><br/>    def test_login(self):<br/>        driver=self.driver<br/>        lp=Login(driver)<br/>&gt;       lp.UserName()<br/><br/>Test/test_login.py:10: <br/>_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ <br/>Pages/LoginPage.py:12: in UserName<br/>    Username=XLutils.readData(path,&#x27;Login&#x27;,r,1)<br/>TestData/XLutils.py:13: in readData<br/>    workbook = openpyxl.load_workbook(sheetName)<br/>../py3-venv/lib/python3.7/site-packages/openpyxl/reader/excel.py:318: in load_workbook<br/>    data_only, keep_links)<br/>../py3-venv/lib/python3.7/site-packages/openpyxl/reader/excel.py:126: in __init__<br/>    self.archive = _validate_archive(fn)<br/>_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ <br/><br/>filename = &#x27;Login&#x27;<br/><br/>    def _validate_archive(filename):<br/>        &quot;&quot;&quot;<br/>        Does a first check whether filename is a string or a file-like<br/>        object. If it is a string representing a filename, a check is done<br/>        for supported formats by checking the given file-extension. If the<br/>        file-extension is not in SUPPORTED_FORMATS an InvalidFileException<br/>        will raised. Otherwise the filename (resp. file-like object) will<br/>        forwarded to zipfile.ZipFile returning a ZipFile-Instance.<br/>        &quot;&quot;&quot;<br/>        is_file_like = hasattr(filename, &#x27;read&#x27;)<br/>        if not is_file_like:<br/>            file_format = os.path.splitext(filename)[-1].lower()<br/>            if file_format not in SUPPORTED_FORMATS:<br/>                if file_format == &#x27;.xls&#x27;:<br/>                    msg = (&#x27;openpyxl does not support the old .xls file format, &#x27;<br/>                           &#x27;please use xlrd to read this file, or convert it to &#x27;<br/>                           &#x27;the more recent .xlsx file format.&#x27;)<br/>                elif file_format == &#x27;.xlsb&#x27;:<br/>                    msg = (&#x27;openpyxl does not support binary format .xlsb, &#x27;<br/>                           &#x27;please convert this file to .xlsx format if you want &#x27;<br/>                           &#x27;to open it with openpyxl&#x27;)<br/>                else:<br/>                    msg = (&#x27;openpyxl does not support %s file format, &#x27;<br/>                           &#x27;please check you can open &#x27;<br/>                           &#x27;it with Excel first. &#x27;<br/>                           &#x27;Supported formats are: %s&#x27;) % (file_format,<br/>                                                           &#x27;,&#x27;.join(SUPPORTED_FORMATS))<br/>&gt;               raise InvalidFileException(msg)<br/><span class="error">E               openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support  file format, please check you can open it with Excel first. Supported formats are: .xlsx,.xlsm,.xltx,.xltm</span><br/><br/>../py3-venv/lib/python3.7/site-packages/openpyxl/reader/excel.py:96: InvalidFileException<br/></div></td></tr></tbody></table></body></html>