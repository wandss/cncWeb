<template>
  <div class="form-group">
    <div class="input-group btn btn-outline-secondary">
      <span class="icon">
        <i class="fa fa-upload"></i>
      </span>
      <label :for="label"> {{label}}</label>
      <input :type="type" :id="label" :required="required"
       @change="$emit('change', $event.target.files)"
      >
    </div>
    <p v-if="filename!==null">
     {{filename[0].name}}
    </p>
  </div>
</template>
<script>
export default {
  name:'Upload',
  model:{
    event:'change',
  },
  props:{
    label:{
      type:String,
      default:'Upload',
      required:true,
    },
    required:{
      type:Boolean,
      default:false
    },
    filename:{
      default:null,
    }
  },
  data(){
    return{
      type:"file"
    }
  },
}
</script>
<style scoped>
.form-group{
  cursor:pointer;
}
input{
  opacity:0;
}
.icon{
  margin-right:2em;
}
</style>
