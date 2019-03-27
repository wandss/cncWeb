<template>
  <div class="container">
    <div class="row mb-4">
      <div class="col-4">
        <card v-for="machine in machines" :header="machine.name"
          cssClass="dark"
          :show="machines.length > 0" :key="machine.name" :hasFooter="true">
          <div slot="content" v-if="isEditing">
            <div v-for="(value, key) in fields" :key="key">
              {{key}} : {{value}}
              <div v-if="value.required && value.type==='string'">
                <base-input type="text" :label="value.label"
                  v-model="value.value"
                  :limit="value.max_length"
                />
              </div>
            </div>
          </div>
          <div slot="content" v-else>
            {{machine.create_date.toLocaleString()}}
          </div>
          <div slot="footer">
            <base-btn cssClass="btn btn-sm btn-warning"
             :hasShadow="false" @click="isEditing=!isEditing">
              Edit
            </base-btn>
          </div>
        </card>
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
import Card from '@/components/card.vue'
import BaseBtn from '@/components/baseButton.vue'
import BaseInput from '@/components/baseInput.vue'
export default {
  name: 'Machines',
  components: {BaseBtn, Card, BaseInput},
  data(){
    return {
      machines: [],
      fields: [],
      isEditing: false,
    }
  },
  created(){
    this.getMachines()
    this.getMachineFields()
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
    },
    getMachineFields(){
      //TODO: Create method to populate fields
      // add a value key to fields object and get this values
      // from macines
      this.$http.options(this.$urls.plot.list)
        .then(resp=>{
          console.log(resp.data)
          this.fields = resp.data.actions.POST
          Object.keys(this.fields).forEach(name=>
            this.machines.forEach(machine=>console.log(machine[name])))
        })
        .catch(error=>{
          console.log(error.response)
        })
    },
  }
}
</script>
<style scoped>
.container{
  margin-top:2rem;
}

</style>
