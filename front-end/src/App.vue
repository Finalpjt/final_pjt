<template>
  <div id="app">
    hello
    <router-link to="/">
    Home
    </router-link>

    <router-link to="/signup">
    Sign Up
    </router-link>

    <router-link to="/profile">
    profile
    </router-link>

    <router-link to="/main">
    main page
    </router-link>

    <!-- <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="navbar-brand">vue-login</div>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/">
            <font-awesome-icon icon="home" /> Home
          </router-link>
        </li>
      </div>
      <div class="navbar-nav ml-auto" v-if="!currentUser">
        <li class="nav-item">
          <router-link to="/signin">
            <font-awesome-icon icon="user-plus" /> Sign Up
          </router-link>
        </li>
        <li class="nav-item">
          <a href="/login" class="nav-link">
            <font-awesome-icon icon="sign-in-alt" /> Login
          </a>
        </li>
      </div>

      <div class="navbar-nav ml-auto" v-if="currentUser">
        <li class="nav-item">
          <router-link to="/profile">
            <font-awesome-icon icon="user" />
            {{username}}
          </router-link>
        </li>
        <li class="nav-item">
          <a href class="nav-link" @click="logOut">
            <font-awesome-icon icon="sign-out-alt" /> LogOut
          </a>
        </li>
      </div>
    </nav> -->
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser () {
      return this.$store.state.auth.user //현재 user 정보
    },
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
      this.$router.push('/')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
