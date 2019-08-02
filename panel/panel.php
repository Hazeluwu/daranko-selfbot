<?php session_start(); /* Starts the session */

if(!isset($_SESSION['UserData']['Username'])){
	header("location:login.php");
	exit;
}
?>

<?php
$page = $_SERVER['PHP_SELF'];
$sec = "1";
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<title>i see you (;</title>
		<meta http-equiv="refresh" content="
			<?php echo $sec?>;URL='
			<?php echo $page?>'">
			<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1">
					<link rel="stylesheet" href="uuu.css">
						<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
						<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
						<style></style>
					</head>
					<body>
						<style>
body {
background-color: #222222
}
</style>
						<?php
    $typing = file('data/typing.txt');
    $send = file('data/send.txt');
    $edited = file('data/edited.txt');
    $deleted = file('data/deleted.txt');
    $groups = file('data/groups.txt');
    $total_dms = file('data/total_dms.txt');
    $total_servers = file('data/total_servers.txt');
    $cmds_send = file('data/cmds_send.txt');
    $bot_info = file('data/bot_data.txt');
    $spam = file('data/spam.txt');
    $cleared = file('data/cleared.txt');
    $saved = file('data/saved.txt');
    $total_logs = file('data/total_logs.txt');
    ?>
						<nav class="navbar navbar-inverse visible-xs">
							<div class="container-fluid">
								<div class="navbar-header">
									<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
										<span class="icon-bar"></span>
										<span class="icon-bar"></span>
										<span class="icon-bar"></span>
									</button>
									<a style="color:green; class="navbar-brand" href="#">Direct Messages Info
									</h2>
								</div>
								<div class="collapse navbar-collapse" id="myNavbar">
									<ul class="nav navbar-nav">
										<li class="active">
											<a href="panel.php">Dashboard</a>
										</li>
										<li>
											<a href="commands.php">Command Responses</a>
										</li>
										<li>
											<a href="dms.php">Dms And Info</a>
										</li>
										<li>
											<a href="server.php">Servers Info</a>
										</li>
									</ul>
								</div>
							</div>
						</nav>
						<div class="container-fluid">
							<div class="row content">
								<div class="col-sm-3 sidenav hidden-xs">
									<h2 style="color:green;">Daranko </h2>
									<ul class="nav nav-pills nav-stacked">
										<li class="active">
											<a href="panel.php">Dashboard</a>
										</li>
										<li>
											<a href="commands.php">Comand Responses</a>
										</li>
										<li>
											<a href="dms.php">Dms And info</a>
										</li>
										<li>
											<a href="servers.php">Servers Info</a>
										</li>
										<li>
											<a style="color:red;" href="logout.php">Logout</a>
										</li>
									</ul>
									<br>
									</div>
									<br>
										<div class="col-sm-9">
											<div class="well">
												<h4 style="color:green;">Dashboard</h4>
												<?php foreach($bot_info as $line) : ?>
												<h5 style="color:red;">[status]
													<?php
              if ($line) :
             echo $line;
              endif; ?>
													<?php endforeach; ?>
												</div>
												<div class="row">
													<div class="col-sm-3">
														<div class="well typing">
															<h4>Typing</h4>
															<?php foreach($typing as $line) : ?>
															<p style="color:coral;">
																<?php
              if ($line) :
             echo $line;
              endif; ?>
																<?php endforeach; ?>
															</div>
														</div>
														<div class="col-sm-3">
															<div class="well send">
																<h4>Send</h4>
																<?php foreach($send as $line) : ?>
																<p style="color:green;">
																	<?php
              if ($line) :
             echo $line;
              endif; ?>
																	<?php endforeach; ?>
																</div>
															</div>
															<div class="col-sm-3">
																<div class="well edited">
																	<h4>Edited</h4>
																	<?php foreach($edited as $line) : ?>
																	<p style="color:orange;">
																		<?php
              if ($line) :
             echo $line;
              endif; ?>
																		<?php endforeach; ?>
																	</div>
																</div>
																<div class="col-sm-3">
																	<div class="well deleted">
																		<h4>Deleted</h4>
																		<?php foreach($deleted as $line) : ?>
																		<p style="color:red;">
																			<?php
              if ($line) :
             echo $line;
              endif; ?>
																			<?php endforeach; ?>
																		</div>
																	</div>
																	<div class="col-sm-3">
																		<div class="well groups">
																			<h4>Groups</h4>
																			<?php foreach($groups as $line) : ?>
																			<p style="color:purple;">
																				<?php
              if ($line) :
             echo $line;
              endif; ?>
																				<?php endforeach; ?>
																			</div>
																		</div>
																		<div class="col-sm-3">
																			<div class="well total-dms">
																				<h4>total dms</h4>
																				<?php foreach($total_dms as $line) : ?>
																				<p style="color:purple;">
																					<?php
              if ($line) :
             echo $line;
              endif; ?>
																					<?php endforeach; ?>
																				</div>
																			</div>
																			<div class="col-sm-3">
																				<div class="well total-servers">
																					<h4>total servers</h4>
																					<?php foreach($total_servers as $line) : ?>
																					<p style="color:purple;">
																						<?php
              if ($line) :
             echo $line;
              endif; ?>
																						<?php endforeach; ?>
																					</div>
																				</div>
																				<div class="col-sm-3">
																					<div class="well cmds-send">
																						<h4>cmds send</h4>
																						<?php foreach($cmds_send as $line) : ?>
																						<p style="color:blue;">
																							<?php
              if ($line) :
             echo $line;
              endif; ?>
																							<?php endforeach; ?>
																						</div>
																					</div>
																					<div class="col-sm-3">
																						<div class="well typing">
																							<h4>Cleared</h4>
																							<?php foreach($cleared as $line) : ?>
																							<p style="color:coral;">
																								<?php
              if ($line) :
             echo $line;
              endif; ?>
																								<?php endforeach; ?>
																							</div>
																						</div>
																						<div class="col-sm-3">
																							<div class="well ggg">
																								<h4>Saved</h4>
																								<?php foreach($saved as $line) : ?>
																								<p style="color:coral;">
																									<?php
              if ($line) :
             echo $line;
              endif; ?>
																									<?php endforeach; ?>
																								</div>
																							</div>
																							<div class="col-sm-3">
																								<div class="well typing">
																									<h4>Spam Send</h4>
																									<?php foreach($spam as $line) : ?>
																									<p style="color:coral;">
																										<?php
              if ($line) :
             echo $line;
              endif; ?>
																										<?php endforeach; ?>
																									</div>
																								</div>
																								<div class="col-sm-3">
																									<div class="well typing">
																										<h4>Total Logs</h4>
																										<?php foreach($total_logs as $line) : ?>
																										<p style="color:coral;">
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
																			</div>
																		</div>
																	</body>
																</html>
