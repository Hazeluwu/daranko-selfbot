<?php session_start(); /* Starts the session */

if(!isset($_SESSION['UserData']['Username'])){
	header("location:login.php");
	exit;
}
?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <title>i see you (;
    </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js">
    </script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js">
    </script>
    <style>
    </style>
  </head>
  <body>
    <style>
      body {
        background-color: #222222
      }
    </style>
    <?php
$servers = file('data/servers.txt');
$total_servers = file('data/total_servers.txt');
?>
    <div class="container-fluid">
      <div class="row content">
        <div class="col-sm-3 sidenav">
          <h3 style="color:green;">Servers Info
          </h3>
          <ul class="nav nav-pills nav-stacked">
            <li class="active">
              <a href="dms.php">Servers Info
              </a>
            </li>
            <li>
              <a href="commands.php">Commands Response
              </a>
            </li>
            <li>
              <a href="#section3">Server Info
              </a>
            </li>
            <li>
              <a href="panel.php">Dashboard
              </a>
            </li>
            <li>
              <a style="color:red;" href="logout.php">Logout
              </a>
            </li>
          </ul>
          <br>
        </div>
        <div class="col-sm-9">
          <?php foreach($total_servers as $line) : ?>
          <h3>
            <small style="color:red;">Servers
              </smal>
            <?php
if ($line) :
echo $line;
endif; ?>
            <?php endforeach; ?>
            <hr>
            <h2 style="color:green;">Server Info
            </h2>
            <?php foreach($servers as $line) : ?>
            <h4 style="color:red;">
              <?php
if ($line) :
echo $line;
endif; ?>
              <?php endforeach; ?>
              </div>
            </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</body>
</html>
