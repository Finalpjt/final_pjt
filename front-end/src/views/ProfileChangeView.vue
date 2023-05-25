<template>
  <div>
    <h1>Profile</h1>
    <form @submit.prevent="profileChange">
      <label for="new_password1"> 비밀번호 : </label>
      <input type="new_password1" id="new_password1" v-model="new_password1">

      <label for="new_password2"> 비밀번호 확인 : </label>
      <input type="new_password2" id="new_password2" v-model="new_password2">

      <input type="submit" value="profileChange">
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileChangeView',

  data() {
    return {
      new_password1: null,
      new_password2: null,
    }
  },
  methods: {

    profileChange() {
      // console.log('signup')
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      const payload = {
        new_password1, new_password2
      }
      this.$store.dispatch('profileChange', payload)
      // this.$router.push('/home')

    }
  }
}
</script>
