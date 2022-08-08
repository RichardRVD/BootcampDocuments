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
				
					<h1 style="margin-left:35%;">
						Here's Your Omikuji!
					</h1>
				
				
					<div class="container-sm" style="background-color: lightblue; width: 540px;">
						<p>In <c:out value="${numbers}"/> years, you will</p>
						<p>live in <c:out value="${city}"/> with</p>
						<p><c:out value="${person}"/> as your</p>
						<p>roommate, selling</p>
						<p><c:out value="${hobby }"/> for a living.</p>
						<p> The next time you see a <c:out value="${living}"/>, you will</p>
						<p>have good luck.</p>
						<p>Also, <c:out value="${nice}"/></p>
					</div>
				
				</div>
				<a style="margin-left: 48%;" href="/omikuji">Go Back</a>
			
		</div>

</body>
</html>