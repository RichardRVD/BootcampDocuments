<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
		<title>Omikuji Form</title>
	</head>
	<body>
		<div class="container">
			<div class="col">
				<h1>
					Send an Omikuji
				</h1>
				<form class="row g-3" action="/submit/omikuji" method="post">
					<label for="numbers">
						Pick any number from 5 to 25:
					</label>
					<input type="number" name="numbers" min="5" max="25">
					<label>
						Enter the name of any city:
					</label>
						<input type="text" name="city">
					<label>
						Enter the name of any real person:
					</label>
					<input type="text" name="person">
					<label>
						Enter professional endeavor or hobby:
					</label>
						<input type="text" name="hobby">
					<label>
						Enter any type of living thing:
					</label>
					<input type="text" name="living">
					<label>
						Say something nice to someone:
					</label>
						<textarea name="nice"></textarea>
					<label>
						Send and show a friend:
					</label>
					<input type="submit" name="Send" value="Send">
				
				</form>
			</div>
		</div>
	<script src="/webjars/jquery/jquery.min.js"></script>
	<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
	</body>
</html>