<template>
  <div>
    <h1>Profile Change</h1>
		<form @submit.prevent="profileChange">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      
      <label for="email">email : </label>
			<input type="text" id="email" v-model="email"><br>

			<input type="submit" value="profileChange">


		</form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      username: this.name,
      password1: this.password1,
      password2: this.password2,
			email: this.email
    }
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/${ this.$route.params.id }/`,
      })
      .then((res) => {
        // console.log(res)
        this.user = res.data
      })
      .catch((err) => {
        // console.log(err)
      })
    },
		profileChange() {
			const username = this.username
			const password1 = this.password1
			const password2 = this.password2
			const email = this.email

			const payload = {
				username, password1, password2, email
			}

			this.$store.dispatch('change', payload)
		}
  }
}
</script>
