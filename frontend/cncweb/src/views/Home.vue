<template>
  <div class="container">
    <div class="form-group">
      <h3>Hello!!!</h3>
      <p>This app controls a Mini CNC Ploting  machine, made with two DVD Drives.</p>
      <p>To start ploting just click the button bellow</p>
      <plot :show="showPlot" @click="showPlot=!showPlot"/>
      <base-btn @click="showPlot=!showPlot">
        Plot
      </base-btn>
      <base-btn @click="$router.push({name: 'machines'})"
        cssClass="btn btn-secondary" >
        My Machines
      </base-btn>
    </div>
  </div>
</template>
<script>
import BaseBtn from '@/components/baseButton.vue'
import Plot from '@/components/plot.vue'

export default {
  name: 'home',
  components: {BaseBtn, Plot},
  data(){
    return {
      showPlot: false,
    }
  },
}
</script>
<style scoped>
.container{
  margin-top:2rem;
}
</style>
