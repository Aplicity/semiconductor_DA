# semiconductor_DA
半导体数据分析

## 数据说明

### 变量名格式：统计指标（过程变量） 加工步骤n，如Mean(APCTemp) 2为加工步骤2中的真空泵温度均值

- **统计指标**
	- Max       -- 最大值  
  - Mean      -- 均值
  - Median    -- 中值
  - Min       -- 最小值
  - Range     -- 最大值-最小值
  - Std Dev   -- 方差
  
- **过程变量**
  - APCPosition      -- 真空泵开度
  - APCTemp          -- 真空泵温度
  - C1PosLo          -- 下电极电容1位置
  - C1PosUp          -- 上电极电容1位置
  - C2PosLo          -- 下电极电容2位置
  - C2PosUp          -- 上电极电容2位置
  - CenterHePressure -- 中央冷却液压力
  - ChamberPressure  -- 反应腔压力
  - EdgeHePressure   -- 边缘冷却液压力
  - ESCCurrent       -- 静电吸盘电流
  - ESCVoltage       -- 静电吸盘电压
  - FlowSplitCenter  -- 花洒中间气体流量
  - FlowSplitEdge    -- 花洒边缘气体流量
  - FlowSplitRatio   -- 花洒中间/边缘气体流量比
  - GAS1Flow         -- 反应气体1流量
  - GAS2Flow         -- 反应气体2流量
  - GAS3Flow         -- 反应气体3流量
  - GAS4Flow         -- 反应气体4流量
  - GAS5Flow         -- 反应气体5流量
  - GAS6Flow         -- 反应气体6流量
  - GAS7Flow         -- 反应气体7流量
  - GAS8Flow         -- 反应气体8流量
  - LowerTemp        -- 底部温度
  - RFPowerLo        -- 下电极微波功率
  - RFPwrUp          -- 上电极微波功率
  - RFRefPowerLo     -- 下电极微波反射功率
  - RFRefPowerUp     -- 上电极微波反射功率
  - RFVdcLo          -- 下电极微波直流电压
  - RFVdcUp          -- 上电极微波直流电压
  - RFVppLo          -- 下电极微波交流电压
  - RFVppUp          -- 上电极微波交流电压
  - TopHVCurrent     -- 顶部高电压电流
  - TopHVVoltage     -- 顶部高电压电压
  - UpperTemp        -- 顶部温度
  - WallTemp         -- 反应腔壁温度
  
  ## 需求
- **分类**
  - 字段'ETCHER'为5个不同的标签，分别代表不同类别的产品。
- **数据分析**
  - 分析字段'ETCH_BIAS_I'、'ETCH_BIAS_R'、'ETCH_BIAS_T'与第几个加工步骤的哪些变量因素有关 
  
