<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>

<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
		<title>Fruity Loops</title>
	</head>
	<body>
	<div class="container">
	
		<h1>Fruit Store</h1>
		<table class="table">
			<tbody>
				<tr>
					<th class="table-info">Name</th>
					<th class="table-info">Price</th>
				</tr>
				<c:forEach var="fruit" items="${fruits}">
				<tr class="table table-dark table-hover">
					<td><c:out value="${fruit.name}"/></td>
					<td><c:out value="${fruit.price}"/></td>
				</tr>
				</c:forEach>
			</tbody>
		</table>
	</div>
	<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
	</body>
</html>