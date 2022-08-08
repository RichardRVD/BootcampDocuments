package com.codingdojo.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.models.User;

@Controller
public class CounterController {
	@RequestMapping("/")
	public String index(HttpSession session, Model model) {
		Integer count = (Integer) session.getAttribute("count");
		if (count == null) {
			session.setAttribute("count", 1);
		} else {
			session.setAttribute("count", count +=1);
		}
		User.add(new User("Ricky"));
		model.addAttribute("name", "Ricky");
		session.setAttribute("name", "Ricky");
		return "index.jsp";
	}
	@RequestMapping("/counter")
	public String counter(HttpSession session, Model model) {
		Integer count = (Integer) session.getAttribute("count");
		model.addAttribute("count", count != null ? count :0);
		return "counter.jsp";
	}
	@RequestMapping("/plus_two")
	public String countPlusTwo(HttpSession session, Model model) {
		Integer count = (Integer) session.getAttribute("count");
		
		if (count == null) {
			session.setAttribute("count",2);
		} else {
			session.setAttribute("count", count += 2);
		}
		model.addAttribute("count", count != null ? count:0);
		return "plus_two.jsp";
	}
	
		
		
	@RequestMapping("/reset")
	public String reset(HttpSession session) {
		session.setAttribute("count", 0);
		return "index.jsp";
	}

}
