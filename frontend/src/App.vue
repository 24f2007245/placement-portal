<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
// import RegisterView from './views/Auth/RegisterView.vue';
</script>

<template>
  <header>
    <div id="top_bar">
      <div class="scale">
        <div class="top_ele" id="rm" >Contact Us | +91 6200209997&emsp;| placementcelladmin@gmail.com&emsp;</div>
        <div class="top_ele ">Application Deadline | 10th April </div>
      </div>
      
    </div>
  </header>
  <!-- <h5>You Are In Home Page</h5> -->

  <RouterView />
</template>

<style scoped>
body{
  margin: 0px;
  padding: 0px;
}

#top_bar{
  
  background-color: #f5f5f5;
  color: #2980b9;
  display: flex;
  justify-content: center;
  

}
.scale{
  display: flex;
  max-width: 1000px;
  /* justify-content: space-between; */
  align-items: center;
  justify-content:center;
  padding: 3px;
  gap: 50px;
}

@media(max-width:855px){
  #top_bar{
    justify-content: center;
    gap: 10px;
    overflow: hidden;
  }
}
@media(max-width:525px){
  /* overflow: hidden; */
  #rm{
    display: none;
  }
  #top_bar{
    display: flex;
    justify-content: center;
    overflow: hidden;
  }

}

</style>
