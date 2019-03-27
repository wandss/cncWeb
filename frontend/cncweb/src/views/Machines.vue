<template>
  <div class="container">
    <div class="row mb-4">
      <div class="col">
        <div v-for="(form, index) in form.data" :key="index">
          <div v-for="(value, key) in form" :key="key">
            {{key}} - {{value}}
            <base-input :label="value.label+':'" type="text"
             v-model="value.value" :limit="value.max_length"
             @input="test(key, value.value)"
            />

          </div>
        </div>
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
import Form from '@/utils/forms.js'
export default {
  name: 'Machines',
  components: {BaseBtn, Card, BaseInput},
  data(){
    return {
      machines: [],
      fields: [],
      isEditing: false,
      form: new Form(),
    }
  },
  mounted(){
    this.getMachines()
  },
  methods: {
    getMachines(){
      this.$http.get(this.$urls.plot.list)
        .then(resp=>{
          this.machines = resp.data.results
          this.getMachineFields()
        })
        .catch(error=>{
          console.log(error.response)
        })
    },
    getMachineFields(){
      this.$http.options(this.$urls.plot.list)
        .then(resp=>{
          this.fields = resp.data.actions.POST
          this.form.metadata = resp.data.actions.POST
          this.form.formData = this.machines.concat()
          this.form.fillForm()
        })
        .catch(error=>{
          console.log(error.response)
        })
    },
    test(key, value){
      // Fix: The $set is add the object key to the object
      // teste: {value: 'Something'}
      // after $set => teste: {value: 'New Value', teste: 'New Value'}
      const index = Object.keys(this.form.metadata).indexOf(key)
      console.log(index)
      this.$set(this.form.data[index][key], key, value)
    }
  }
}
</script>
<style scoped>
.container{
  margin-top:2rem;
}

</style>
