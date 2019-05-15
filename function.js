  function validate_row() {
    let value = parseInt(document.getElementById('row').value)

    if (value > 14) {
      document.getElementById('row').value = 14
    }
  }

  function scrapping() {

    let row = parseInt(document.getElementById('row').value),
        table = document.getElementById('table').getElementsByTagName('tbody')[0],
        crawlmessage = document.getElementById('crawl-message');

    if (row > 0) {

      crawlmessage.classList.add("show");

      if (table.rows.length > 0) {
        for (var i = 0; i < table.rows.length; i++) {
          table.deleteRow(i);
        }
      }

      var {PythonShell} = require("python-shell"),
          path = require("path"),
          options = {
            scriptPath : path.join(__dirname, '/./core/'),
            args : [row]
          }

      PythonShell.run('core.py', options, function (err, results) {
        if (err) throw err;

        no = 0;
        html = '';

        data = JSON.parse(results)
        data.forEach(function(value) {
            no++;
            let parse = value.split('--');

            var row = table.insertRow(0);

            var cell = row.insertCell(0);
            var cell2 = row.insertCell(1);

            cell.innerHTML = parse[0];
            cell2.innerHTML = parse[1];

            crawlmessage.classList.remove("show");
        });
      });

    } else {
      alert('lengkapi dlu inputnya mas broo')
    }

  }

  function openExternal(link) {
    require("electron").shell.openExternal(link);
  }
