<template>
    <canvas ref="chart" width="400px" height="400px">
    </canvas>
</template>
<script>
    import ChartUtils from '@/components/charts/utils';

    export default{
        name:'LineChart',
        props:{
            chartData:{
                type:Array,
                default:()=>[],
            },
            title:{
                type:String,
                default:''
            },
            showLegend:{
                type:Boolean,
                default:true
            },
            showTooltips:{
                type:Boolean,
                default:true,
            },
            fill:{
                type:Boolean,
                default:false,
            },
            lineTension:{
                type:Number,
                default:0,
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
            showLegend(){
                this.createChart()
            },
            showTooltips(){
                this.createChart()
            },
            fill(){
                this.createChart()
            },
            lineTension(){
                this.createChart()
            }
        },
        methods:{
            createChart(){
                if(this.chartData.length >0 ){
                    const chartData  = new ChartUtils(this.chartData,
                        this.lineTension, this.fill);
                    chartData.setDataset()
                    const datasets = chartData.datasets;
                    new this.$chart(this.$refs.chart,{
                        type:'line',
                        data:{
                            labels:datasets.labels,
                            datasets:datasets.data,
                        },
                        options:{
                            title:{
                                display:this.title.length > 0,
                                text:this.title,
                                fontSize:16,
                                fontStyle:'bold',
                            },
                            legend:{
                                display:this.showLegend,
                                position:'bottom',
                                fullWidth:true,
                            },
                            tooltips:{
                                enabled:this.showTooltips,
                            },
                            scales:{
                                yAxes:[{
                                    ticks:{
                                        beginAtZero:true,
                                    }
                                }],
                            },
                            showLines:true,
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
