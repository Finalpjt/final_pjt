<template>
  <div id="app">
    <router-link to="/">
    Home
    </router-link>
    |
    <router-link to="/profile">
    profile
    </router-link>
    |
    <router-link to="/main">
    main page
    </router-link>
    |
    <router-link v-if="!isLogin" to="/signup">
    Sign Up
    </router-link>

    <input type="text" v-model="searchkey" @keyup.enter="search()" value="search">
    <button @click="search()">search</button>

    <button v-if="isLogin" @click="logout">logout</button>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchkey: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
    },
    search() {
      const searchkey = this.searchkey
      const payload = {
        searchkey
      }
      this.$store.dispatch('search', payload)
    },
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
