<template>
    <div style="{height}">
        <canvas ref="chart">
        </canvas>
    </div>
</template>
<script>
    import ChartUtils from '@/components/charts/utils';

    export default{
        name:'Pie',
        props:{
            chartData:{
                type:Array,
                default:()=>[],
            },
            title:{
                type:String,
                default:''
            },
            innerRadius:{
                type:Number,
                default:0,
            },
            showLegend:{
                type:Boolean,
                default:true
            },
            legendPosition:{
                type:String,
                default:'top',
            }
        },
        data(){
            return{
                chart:null,
            }
        },
        mounted(){
            this.createChart()
        },
        watch:{
            chartData(){
                this.createChart()
            },
            title(){
                this.createChart()
            },
            innerRadius(){
                this.createChart()
            },
            showLegend(){
                this.createChart()
            },
            legendPosition(){
                this.createChart()
            },
        },
        methods:{
            createChart(){
                if(this.chartData.length > 0){
                    if(this.chart){
                        this.chart.destroy()
                    }
                    const chartData  = new ChartUtils(this.chartData)
                    chartData.setDataset('pie')
                    const datasets = chartData.datasets;
                    this.chart = new this.$chart(this.$refs.chart,{
                        type:'pie',
                        data:{
                            datasets:datasets.data,
                            labels:datasets.labels,
                        },
                        options:{
                            cutoutPercentage:this.innerRadius,
                            title:{
                                display:this.title.length > 0,
                                text:this.title,
                                fontSize:16,
                                fontStyle:'bold',
                            },
                            legend:{
                                display:this.showLegend,
                                position:this.legendPosition,
                            }
                        }
                    })
                }
            },
        }
    }
</script>
<style scoped>
#chart{
    width:450px;
    height:200px;
}
</style>
