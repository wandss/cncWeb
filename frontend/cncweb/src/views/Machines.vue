<template>
  <div class="container">
    <div class="row mb-4">
      <div class="col">
       Cards with MACHINES LIST HERE
       {{machines}}
      </div>
    </div>
    <div class="row">
      <div class="col">
        <base-btn>
          Add
        </base-btn>
      </div>
    </div>
  </div>
</template>
<script>
import BaseBtn from '@/components/baseButton.vue'
export default {
  name: 'Machines',
  components: {BaseBtn},
  data(){
    return {
      machines: [],
    }
  },
  created(){
    this.getMachines()
  },
  methods: {
    getMachines(){
      this.$http.get(this.$urls.plot.list)
        .then(resp=>{
          this.machines = resp.data.results
        })
        .catch(error=>{
          console.log(error.response)
        })
    }
  }
}
</script>
<style scoped>
.container{
  margin-top:2rem;
}

</style>
