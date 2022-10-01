<template>
  <!-- <Index/> -->
  <!-- 舉例用的頁面 -->
  <!-- <Navbar/> -->
  <router-view></router-view>
</template>

<script>
// import Navbar from './components/Navbar.vue'
// import Index from './page/Index.vue'
localStorage.userid=''
export default {
  name: 'App',
  components: {
    //Navbar
    //Index
  }
}

</script>

<style>
/* 這裡可以寫全域的css，但通常我會放一個 all.scss 在 assets 裡方便找 */
</style>
<!-- npm run serve -->