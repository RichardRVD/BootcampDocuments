package com.codingdojo.controllers;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DaikichiController {
	@RequestMapping( "/daikichi" )
	public String daikichiPage() {
		return "<h1>Welcome!</h1>";
	}
	@RequestMapping("/daikichi/today")
	public String daikichiToday() {
		return "<h1>Today you will find luck in all your endeavors!</h1>";
	}
	@RequestMapping("/daikichi/tomorrow")
	public String daikichiTomorrow() {
		return "<h1>Tomorrow, an opportunity will arise, so be sure to be open to new ideas!</h1>";
	}
	@RequestMapping("/daikichi/travel/{city}")
	public String cityTravel(@PathVariable("city")String city) {
		return "Congratulations! You will soon travel to" + " " + city+"!";
	}
	@RequestMapping("/daikichi/lotto/{number}")
	public String lottoNum(@PathVariable("number")int number) {
		if(number %2==0) {
			return "You will take a grand journey in the near future, but be weary of tempting offers";
		} else {
		return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends";
		}
	}
}
