<template>
  <div class="input-group mb-3">
    <div class="input-group-prepend" v-if="leftLabel !== undefined">
      <label class="input-group-text" for="inputGroupSelect01">
        {{leftLabel}}
      </label>
    </div>
    <select class="custom-select" id="inputGroupSelect01"
      v-if="options.length !== 0" 
      @input="$emit('input', $event.target.value)">
      <option :selected="selected===null" :value="null">Choose...</option>
      <option v-for="opt in options" :value="opt.id"
       :key="opt[optionName]" :selected="selected===opt[optionName]"
      >
       {{opt[optionName]}}
      </option>
    </select>
    <select v-else class="custom-select">
      <option >Loading...</option>
    </select>
    <div class="input-group-append" 
     v-if="appendedButtons.length>0 && options.length !== 0">
      <button v-for="btn in appendedButtons" :key="btn.name"
      :class="'btn btn-outline-'+btn.cssClass"
      :disabled="btn.disabled"
      @click="btn.event"
      :type="btn.type"
      >
      <span :class="btn.icon"></span>
        {{btn.name}}
      </button>
    </div>
  </div>
</template>
<script>

export default{
    name:'baseSelect',
    props:{
        leftLabel:{
            type:String,
        },
        options:{
            type:Array,
            required:true,
            default:()=>[],
        },
        optionName:{
            type:String,
            required:true,
        },
        selected:{
            type:String,
            default:'',
        },
        appendedButtons:{
            type:Array,
            default:()=>[],
        },
    },
}
</script>
<style>
</style>
