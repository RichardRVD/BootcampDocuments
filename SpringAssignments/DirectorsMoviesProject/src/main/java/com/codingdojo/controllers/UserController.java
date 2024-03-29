package com.codingdojo.controllers;

import java.util.ArrayList;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.models.User;

@Controller
public class UserController {
	
	
	@RequestMapping("/")
	public String displayLogin() {
		return "index.jsp";
	}
	@RequestMapping(value="/process/login", method=RequestMethod.POST)
	public String processLogin(@RequestParam(value="userName") String userName, @RequestParam(value="password") String password, HttpSession session, RedirectAttributes redirectAttributes) {
		
		ArrayList<User> listOfUsers= new ArrayList<User>();
		User user1 = new User("Alexander", "Miller", "alex08", "pass12345");
		User user2 = new User("Martha", "Speaks", "speaks08", "pass12345");
		listOfUsers.add(user1);
		listOfUsers.add(user2);
		
		for( int i = 0; i <listOfUsers.size(); i++) {
			if(listOfUsers.get(i).getUserName().equals(userName) && listOfUsers.get(i).getPassword().equals(password)) {
				session.setAttribute("firstName", listOfUsers.get(i).getFirstName());
				session.setAttribute("lastName", listOfUsers.get(i).getLastName());
				return "redirect:/home";
			}
		}
		redirectAttributes.addFlashAttribute("errorLogin", "Invalid Credentials");
		
		System.out.println("Username: " + userName + " " + "Password: " + password);
		
		return "redirect:/";
		
	}
	@RequestMapping(value="/home")
	public String displayHome() {
		return "home.jsp";
	}

}
