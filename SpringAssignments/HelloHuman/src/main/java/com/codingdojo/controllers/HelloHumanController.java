package com.codingdojo.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloHumanController {
	
	@RequestMapping("/")
	public String helloUser(@RequestParam(value = "firstName", required = false)String firstName, @RequestParam(value="lastName", required = false)String lastName) {
		if(firstName == null && lastName == null) {
			return "Hello Human";
		} else {
		System.out.println(firstName);
		return "Hello" +" "+ firstName + " " + lastName;
		}
	}
}
