<template>
  <div class="mb-3">
    <label v-if="label.length>0">
      {{label}}
    </label>
    <div :class="'input-group input-group-'+size">
      <div class="input-group-prepend">
        <span v-if="limit !== undefined"
         :class="['input-group-text',{'outOfSpace':value.length===limit}]">
         {{limit - value.length}}
        </span>
        <button  v-for="btn in prependedButtons"
         :key="btn.name"
         :class="'btn btn-outline-'+btn.cssClass"
         @click="btn.event" :disabled="btn.disabled"
         >
        <span :class="btn.icon"></span>
          {{btn.name}}
        </button>
      </div>
      <input @input="handleInput($event)"
       :class="['form-control', value.length === limit? 'outOfSpace':'']"
       :type="type"
       :placeholder="placeholder"
       :disabled="disabled"
       :maxlength="limit"
       :value="value"
      />
      <div class="input-group-append" v-if="appendedButtons.length>0">
        <button  v-for="btn in appendedButtons" :key="btn.name"
         :class="'btn btn-outline-'+btn.cssClass"
         @click="btn.event" :disabled="btn.disabled"
         >
          <span :class="btn.icon"></span>
          {{btn.name}}
        </button>
      </div>
    </div>
    <alert :cssClass="alert.css" :show="alert.show" :title="alert.title">
      {{alert.message}}
    </alert>
  </div>
</template>
<script>
import validate from '@/components/utils/input.js';
import alert from '@/components/Alert';

export default{
  name:'AppInput',
  components:{alert},
  props:{
    type:{
      type:String,
      required:true,
      default:'text',
    },
    label:{
      type:String,
      default:'',
    },
    placeholder:{
      type:String,
    },
    disabled:{
      type:Boolean,
      default:false,
    },
    limit:{
      type:Number,
    },
    value:{
      default:'',
    },
    prependedButtons:{
      type:Array,
      default:()=>[],
    },
    appendedButtons:{
      type:Array,
      default:()=>[],
    },
    size:{
      type:String,
      default:'',
    },
  },
  data(){
    return{
      alert:{},
    }
  },
  methods:{
    handleInput(e){
      let value = e.target.value;

      if(this.type === 'datetime' && value.length >= 0){
        value = validate.date(value)
        this.alert = value.alert
        value = value.value
      }

      this.$emit('input', value)
    }
  }
}
</script>
<style scoped>
input{
    border-radius:0;
}
span{
    border-radius:0;
}
.outOfSpace{
    border-color:red;
    color:red;
    box-shadow: 1px 0px 2px 2px red;
}

</style>
