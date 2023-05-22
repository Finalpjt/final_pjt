<template>
  <div id="home">
    <h1>Home Page</h1>
    <h2>Login</h2>
    <div v-if="this.isLogin">
      isLogin.
      <br>
      <input type="text" v-model="searchkey" @keyup.enter="search()" value="search">
      <button @click="search()">search</button>
    </div>
    <div v-if="!this.isLogin">
      <label for="username">사용자명 : </label>
      <input @keyup.enter="Cursor_password" ref="cursor" type="text" id="username" v-model="username"><br>

      <label for="password"> 비밀번호 : </label>
      <input @keyup.enter="login" ref="cursor_password" type="password" id="password" v-model="password"><br>

      <input @click="login" type="submit" value="확인">
      <router-link v-if="!isLogin" to="/signup">
      회원가입
      </router-link>
    </div>

<!--   <ul class=""> -->
      <!-- 비 로그인 시  -->
      <!-- <div class="navbar-nav ml-auto" v-if="!currentUser">
        <li class="nav-item">
          <router-link to="/signup">
            <font-awesome-icon icon="user-plus" /> Sign Up
          </router-link>
        </li>
        <li class="nav-item">
          <form @submit.prevent="logIn">
            <label for="username">username : </label>
            <input type="text" id="username" v-model="username"><br>

            <label for="password"> password : </label>
            <input type="password" id="password" v-model="password"><br>

            <input type="submit" value="logIn">
          </form>
        </li>
      </div>
      로그인 시
      <div class="navbar-nav ml-auto" v-if="currentUser">
        <li class="nav-item">
          <router-link to="/profile">
            <font-awesome-icon icon="user" />
            {{currentUser.username}}
          </router-link>
        </li>
        <li class="nav-item">
          <a href class="nav-link" @click="logout">
            <font-awesome-icon icon="sign-out-alt" /> LogOut
          </a>
        </li>
      </div>
    </ul> -->

  </div>
</template>

<script>

// @ is an alias to /src

export default {
  name: 'HomeView',
  data() {
    return {
      username: null,
      password: null,
      searchkey: null,
    }
  },
  mounted() {
    this.startCursor()
  },
  
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

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    },
    search() {
      const searchkey = this.searchkey
      const payload = {
        searchkey
      }
      this.$store.dispatch('search', payload)
    },
    startCursor() {
      this.$refs.cursor.focus()
    },
    Cursor_password() {
      this.$refs.cursor_password.focus()
    }
  }
}
</script>
