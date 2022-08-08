<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>

<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
		<title>Counter Up</title>
	</head>
	<body>
		<div>
			<table>
				<tr>
					<td>You have visited <a href="http://localhost:8080" >http://localhost:8080 </a><c:out value="${count}"/> times.</td>
				</tr>
				<tr>
					<td><a href="http://localhost:8080">Test another visit?</a></td>
				</tr>	
			</table>
			<a class="button btn-danger" href="http://localhost:8080/reset">Reset</a>
		</div>
	
	
		<script src="/webjars/jquery/jquery.min.js"></script>
		<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
	</body>
</html>