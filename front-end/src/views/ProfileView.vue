<template>
  <div>
    <h1>Profile</h1>
    사용자명 : {{ username }}
    <br>
    사용자 이메일 : {{ email }}
    <br>
    <!-- 사용자 닉네임 : {{ nickname }} -->
    <router-link to="/profilechange">changepassword</router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      user: null,
      username: null,
      email: null,
      // nickname: null,
    }
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      const token = this.$store.state.token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
        Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        // console.log(token)
        this.user = res.data
        this.username = res.data.username
        this.email = res.data.email
        // this.nickname = res.data.nickname
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
