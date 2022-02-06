<template>
	<div>
		<div class="main">
			<div v-show="!displayResults">
				<textarea id="textarea" v-model="text" autofocus maxlength=200 placeholder="News Headline/Title"></textarea><br />
				<button id="clearBtn" @click="text=''">Clear Text</button>
				<button @click="getResults">Get Result</button>
			</div>
			<div v-show="displayResults">
				<Results :text="text" :result="result"/>
				<button @click="displayResults = false">Try Again</button>
			</div>
		</div>
	</div>
</template>

<script>
import Results from "./Results.vue";

export default {
	name: "Main",
	components: { Results },
	data() {
		return {
			text: "",
			displayResults: false,
			result: {"abc": 80},
		};
	},
	methods: {
		getResults() {
			if (this.$data.text === "") {
				document.getElementById("textarea").classList.add("errText");
			} else {
				document.getElementById("textarea").classList.remove("errText");
				this.$data.displayResults = true;
				// const requestOptions = {
				// 	method: "POST",
				// 	headers: { "Content-Type": "application/json" },
				// 	body: JSON.stringify({ text: this.$data.text })
				// };
				// fetch("http://127.0.0.1:5000", requestOptions)
				// 	.then(response => response.json())
				// 	.then(data => (this.$data.result = data.Results));
			}
		}
	}
};
</script>

<style scoped>
.main {
	margin: auto;
	width: 70%;
}

textarea {
	outline: none !important;
	height: 100px;
	width: 50%;
	padding: 12px 20px;
	box-sizing: border-box;
	resize: none;
}

.errText {
	border: 3px dotted red;
}
button {
	margin: auto;
	margin-top: 8px;
	position: relative;
	background-color: #4caf50;
	border: 2px solid #4caf50;
	font-size: 20px;
	color: aliceblue;
	padding: 20px;
	width: 150px;
	text-align: center;
	transition-duration: 0.4s;
	text-decoration: none;
	overflow: hidden;
	cursor: pointer;
}

button:hover {
	opacity: 0.8;
	transition: opacity 0.8s;
}

#clearBtn {
	margin-right: 8px;
	background-color: #fff;
	color: #4caf50;
	border: 2px solid #4caf50;
}
#clearBtn:hover {
	color: #fff;
	background-color: #4caf50;
	opacity: 1;
	transition: opacity 0.8s;
}
</style>