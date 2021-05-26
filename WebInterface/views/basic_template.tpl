<!DOCTYPE html>
<html>
<body>

<h2>{{current_directory}}</h2>

<form action="/upload" method="post" enctype="multipart/form-data">
  <p>Observation Number:<input type="number" name="obs_num" min="1" max="8">
  <p>Select a file: <input type="file" name="upload" />
  <p><input type="submit" value="Start upload" />
</form>
 
</body>
</html>
