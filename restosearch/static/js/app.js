class Zomato {
	constructor() {
		this.header = {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			credentials: 'same-origin'
		}
	}

	// fetch("/searchresto/", {
 //              method: 'POST',
 //              body: data,
 //              credentials: 'same-origin',
 //            }

	async searchAPI(lat,lng,radius,city) {
		//request url
		console.log(lat,lng,radius,city)
		const URL = `/searchresto/`;
		//city url
		// const cityURL = `https://developers.zomato.com/api/v2.1/cities?q=${city}
		// `

		// //category data
		// const categoryInfo = await fetch(categoryURL, this.header)
		// const categoryJSON =  await categoryInfo.json();
		// const categories = await categoryJSON.categories;

		// //search city
		// const cityInfo = await fetch(cityURL, this.header);
		// const cityJSON = await cityInfo.json()

		// const cityLocation = await cityJSON.location_suggestions;
		 
		// let cityID = 0
		// if(cityLocation.length !== 0) {
		// 	cityID = await cityLocation[0].id
		// }

		// //search restaurant 
		// const restaurantURL = `https://developers.zomato.com/api/v2.1/search?entity_id=${cityID}&entity_type=city&category=${categoryID}&sort=rating
		// `
		// const restaurantInfo = await fetch(restaurantURL, this.header)
		// const restaurantJSON = await restaurantInfo.json()
		// const restaurants = await restaurantJSON.restaurants



		
		return {
			categories,
			cityID,
			restaurants
		}
	}
}

class UI {
	constructor() {
		this.loader = document.querySelector('.loader');
		this.restaurantList = document.querySelector('#restaurant-list')
	}

	showLoader() {
		this.loader.classList.add('showItem');
	}
	hideLoader() {
		this.loader.classList.remove('showItem')
	}

	getRestaurants(restaurants) {
		this.hideLoader()
		if(restaurants.length === 0) {
			this.showFeedback('no such categories exist in the selected city')
		} else {
			this.restaurantList.innerHTML = '';
			restaurants.forEach(restaurant => {
				const { thumb:img, name, location:{address}, user_rating:{aggregate_rating}, cuisines, average_cost_for_two:cost,menu_url,url } = restaurant.restaurant;

				if(img !== '') {
					this.showRestaurant(img, name, address, aggregate_rating,cuisines,cost,menu_url,url )
				}
			})
		}
	}

	showRestaurant(img, name, address, aggregate_rating, cuisines,cost,menu_url,url) {
		const div = document.createElement('div');
		div.classList.add('col-11', 'mx-auto', 'my-3', 'col-md-4');

		div.innerHTML = `
				<div class="card">
				<div class="card">
				<div class="row p-3">
				<div class="col-5">
					<img src="${img}" class="img-fluid img-thumbnail" alt="">
				</div>
				<div class="col-5 text-capitalize">
					<h6 class="text-uppercase pt-2 redText">${name}</h6>
					<p>${address}</p>
				</div>
				<div class="col-1">
					<div class="badge badge-success">
					${aggregate_rating}
					</div>
				</div>
				</div>
				<hr>
				<div class="row py-3 ml-1">
				<div class="col-5 text-uppercase ">
					<p>cousines :</p>
					<p>cost for two :</p>
				</div>
				<div class="col-7 text-uppercase">
					<p>${cuisines}</p>
					<p>${cost}</p>
				</div>
				</div>
				<hr>
				<div class="row text-center no-gutters pb-3">
				<div class="col-6">
					<a href="${menu_url}" target="_blank" class="btn redBtn  text-uppercase"><i class="fas fa-book"></i> menu</a>
				</div>
				<div class="col-6">
					<a href="${url}" target="_blank" class="btn redBtn  text-uppercase"><i class="fas fa-book"></i> website</a>
				</div>
				</div>
				</div>
			</div>
		`
		this.restaurantList.appendChild(div)
	}
}



(function(){
	const restofindform = document.getElementById('restofindform')
	// const searchCity = document.getElementById('searchCity')
	// const searchCategory = document.getElementById('searchCategory')
	// const lat=document.getElementById("user_lat").value
 //    const lng=document.getElementById("user_long").value
 //    const radius=document.getElementById("user_radius").value
 //    const city=document.getElementById("pac-input").value

	// const zomato = new Zomato()
	

	const ui = new UI()

	//add select options
	// document.addEventListener('DOMContentLoaded', () => {
	// 	//logic goes here
	// 	zomato.searchAPI()
	// 	.then(data => {
	// 		ui.addSelectOptions(data.categories)
	// 	})
	// })

	//submit form
	restofindform.addEventListener('submit', e => {
		e.preventDefault()
		if(city != '') {
			//logic goes if populated values
			zomato.searchAPI(cityValue)
			.then(data => {
				if(data.cityID !== 0) {
					// console.log(data.cityID)
					ui.showLoader()
					zomato.searchAPI(cityValue, categoryValue)
					.then(data => {
						ui.getRestaurants(data.restaurants)
					})
				} else {
					ui.showFeedback('Please enter a valid city')
				}
			})
		} else {
			ui.showFeedback('please enter a city and select category')
		}
	})



})()