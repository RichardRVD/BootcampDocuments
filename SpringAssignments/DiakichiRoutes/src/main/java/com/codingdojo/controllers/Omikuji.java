package com.codingdojo.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class Omikuji {
	
	@RequestMapping(value="/omikuji")
	public String displayOmikuji() {
		return "index.jsp";
	}
	
	@RequestMapping(value="/submit/omikuji", method=RequestMethod.POST)
	public String processOmikuji(HttpSession session, @RequestParam(value="numbers") Integer numbers,
								 @RequestParam(value="city") String city,
								 @RequestParam(value="person") String person,
								 @RequestParam(value="hobby") String hobby,
								 @RequestParam(value="living") String living,
								 @RequestParam(value="nice") String nice) {
		
		session.setAttribute("numbers", numbers);
		session.setAttribute("city", city);
		session.setAttribute("person", person);
		session.setAttribute("hobby", hobby);
		session.setAttribute("living", living);
		session.setAttribute("nice", nice);
		return "redirect:/omikuji/show";
	}
	@RequestMapping(value="/omikuji/show")
	public String displayOmikujiShow() {
		return "show.jsp";
	}

}
