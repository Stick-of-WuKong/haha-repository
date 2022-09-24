// package chap3.example;
public class Cp{
	public static void main(String[] args) {
		boolean[] red = new boolean[34];   //红色球，使用下标1-33的元素,默认值为false
		boolean[] blue = new boolean[17];   //红色球，使用下标1-16的元素
		System.out.println("准备开奖......");
		//选择6个红球
		int count=1;
		while(count<7){  //不足6个时继续选择红球
			int selectedPos = (int)(Math.random()*33)+1;  //生成随机数[1,33]
			if(red[selectedPos]==false){  //未选过的红球可以被选
				red[selectedPos]=true;   //置已被选标记
				count++;  
			}
		}
		//开奖--选择一个蓝色球
		int selectedPos = (int)(Math.random()*16)+1;
		blue[selectedPos]=true;
		
		//输出开奖结果
		System.out.print("红色球编号为：");
		for(int i=1; i<red.length; i++){
			if(red[i]==true){
				System.out.print((i<10?"0"+i:i)+"  ");
			}
		}
		
		System.out.printf("\n蓝色球编号为：");
		for(int i=1; i<blue.length; i++){
			if(blue[i]==true){
				System.out.print((i<10?"0"+i:i)+"  ");
			}
		}
		System.out.println();
		System.out.println("201883290417于海航");
	}

}
