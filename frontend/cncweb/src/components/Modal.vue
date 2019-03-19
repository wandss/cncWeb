<template>
    <Overlay :show="show">
        <div :class="['modal-dialog', modalSize]">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">
                        {{title}}
                    </h5>
                    <button type="button" class="close" @click="$emit('click')">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <slot name="body"></slot>
                </div>
                <div class="modal-footer" >
                    <slot name="footer"></slot>
                </div>
            </div>
        </div>
    </Overlay>
</template>
<script>
import Overlay from '@/components/Overlay';
export default{
    name:'Modal',
    components:{Overlay},
    props:{
        title:{
            type:String,
            required:true,
            default:'Modal Title'
        },
        modalSize:{
            defalt:'modal-sm'
        },
        hasFooter:{
            type:Boolean,
            default:false,
        },
        show:{
            type:Boolean,
            default:false,
            required:true,
        }
    }

}
</script>
<style>
.modal-full{
    max-width:98% !important;
}
</style>
