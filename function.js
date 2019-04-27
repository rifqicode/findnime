  // my script
  function validate_page() {
    let value = parseInt(document.getElementById('page').value)

    if (value > 3) {
      document.getElementById('page').value = 3
    }
  }

  function validate_row() {
    let value = parseInt(document.getElementById('row').value)

    if (value > 14) {
      document.getElementById('row').value = 14
    }
  }

  function scrapping() {
    let page = parseInt(document.getElementById('page').value),
        row = parseInt(document.getElementById('row').value),
        table = document.getElementById('table').getElementsByTagName('tbody')[0];

    if (page > 0 && row > 0) {

      var {PythonShell} = require("python-shell"),
          path = require("path"),
          options = {
            scriptPath : path.join(__dirname, '/./core/'),
            args : [page , row]
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
            // Create an empty <tr> element and add it to the 1st position of the table:
            var row = table.insertRow(0);
            // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);

            // Add some text to the new cells:
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
