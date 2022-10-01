<template>
  <Navbar/>
  <span v-if=log()>
    現在的使用者是{{USER}}
  </span>
  <Carousel/>
  <!-- <SearchBar/> -->
  <Card/>
</template>

<script>
import Carousel from '@/components/Carousel.vue'
import Card from '@/components/ItemCard.vue'
import Navbar from '@/components/Navbar.vue'
// // import SearchBar from '@/components/SearchBar.vue'

export default {
  name: "Index",
  data() {
    return {
      USER:localStorage.userid,
    }
  },
  mounted(){
    //localStorage.userid=''
    console.log("ID=",localStorage.userid)
  },
  components: {
    Navbar,
    Carousel,
    Card,
    // SearchBar,
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

