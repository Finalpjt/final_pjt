<template>
  <div id="home">
    <h1>Home Page</h1>
    <h2>Login</h2>
    <div v-if="this.isLogin">
      isLogin.{{username}}
      <br>
      <!-- <input type="text" v-model="searchkey" @keyup.enter="search()" value="search">
      <button @click="search()">search</button> -->
    </div>
    <div v-if="!this.isLogin">
      <label for="username">사용자명 : </label>
      <input @keyup.enter="Cursor_password" ref="cursor" type="text" id="username" v-model="username"><br>

      <label for="password"> 비밀번호 : </label>
      <input @keyup.enter="login()" ref="cursor_password" type="password" id="password" v-model="password"><br>

      <input @click="login" type="submit" value="확인">
      <router-link v-if="!isLogin" to="/signup">
      회원가입
      </router-link>
    </div>
    <MovieRecommend />
  </div>
</template>

<script>
import MovieRecommend from '@/components/MovieRecommend.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {

  MovieRecommend,

  },
  data() {
    return {
      username: null,
      password: null,
      searchkey: null,
    }
  },
  // mounted() {
  //   if(!this.login){this.startCursor()}
  // },
  
  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  
  methods: {
    logout () {
      this.$store.dispatch('/logout')
    },
    login() {
      const username = this.username
      const password = this.password
      console.log(username)

      if (!username) {
        alert('ID 입력해주세요')
        return
      } else if (!password){
        alert('비밀번호 입력해주세요')
        return
      }

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    },
    // search() {
    //   const searchkey = this.searchkey
    //   const payload = {
    //     searchkey
    //   }
    //   this.$store.dispatch('search', payload)
    // },

    // startCursor() {
    //   this.$refs.cursor.focus()
    // },
    Cursor_password() {
      this.$refs.cursor_password.focus()
    }
  }
}
</script>
