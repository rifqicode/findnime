  function validate_row() {
    let value = parseInt(document.getElementById('row').value)

    if (value > 14) {
      document.getElementById('row').value = 14
    }
  }

  function scrapping() {

    let row = parseInt(document.getElementById('row').value),
        table = document.getElementById('table').getElementsByTagName('tbody')[0];

    if (row > 0) {

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

            let index = table.rows.length + 1
            var row = table.insertRow(0);

            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);

            cell1.innerHTML = no;
            cell2.innerHTML = parse[0];
            cell3.innerHTML = parse[1];
        });
      });

    } else {
      alert('lengkapi dlu inputnya mas broo')
    }

  }

  function openExternal(link) {
    require("electron").shell.openExternal(link);
  }
