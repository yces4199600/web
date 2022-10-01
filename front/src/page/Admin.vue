<template>
  <Navbar/>
  <span v-if=log()>
    現在的使用者是{{USER}}
  </span>
  <Carousel/>
  <Card/>
</template>

<script>

import Carousel from '@/components/Carousel.vue'
import Card from '@/components/ItemCard.vue'
import Navbar from '@/components/Navbar.vue'



export default {
  name: "admin",
  data() {
    return {
      USER:localStorage.userid
    }
  },
  // computed: {
  //   USER: function () {
  //     return 
  //   },
  // },
  components: {
    Navbar,
    Carousel,
    Card,
  },
    methods:{
    log(){
      console.log("show")
      if(localStorage.userid == ''){
        return false
      }
      else{
        return true
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
