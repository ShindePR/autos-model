
## utils file
import pickle
import json
import pandas as pd
import numpy as np
import config


class CarPrice():
    def __init__ (self,symboling, normalized_losses, fuel_type, aspiration,
       num_of_doors, drive_wheels,engine_location,wheel_base,
       length, width,height,curb_weight,num_of_cylinders,
       engine_size,bore,stroke,compression_ratio,horsepower,
       peak_rpm,city_mpg,highway_mpg,body_style,
       engine_type, 
       fuel_system):
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.body_style = "body-style_"+body_style
        self.engine_type = "engine-type_"+engine_type
        self.fuel_system = "fuel-system_"+fuel_system

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        body_style_index = self.json_data['column'].index(self.body_style)
        engine_type_index = self.json_data['column'].index(self.engine_type)
        fuel_system_index = self.json_data['column'].index(self.fuel_system)

        array = np.zeros(len(self.json_data['column']))

        array[0]=self.symboling
        array[1]=self.normalized_losses
        array[2]=self.json_data['fuel_type'][self.fuel_type]
        array[3]=self.json_data["aspiration"][self.aspiration]
        array[4]=self.json_data["num_of_doors"][self.num_of_doors]
        array[5]=self.json_data["drive_wheels"][self.drive_wheels]
        array[6]=self.engine_location
        array[7]=self.wheel_base
        array[8]=self.length
        array[9]=self.width
        array[10]=self.curb_weight
        array[11]=self.num_of_cylinders
        array[12]=self.engine_size
        array[13]=self.bore
        array[14]=self.stroke
        array[15]=self.compression_ratio
        array[16]=self.horsepower
        array[17]=self.peak_rpm
        array[18]=self.city_mpg
        array[19]=self.highway_mpg

        array[body_style_index]=1
        array[engine_type_index]=1
        array[fuel_system_index]=1

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        #print("predicted_car",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    symboling=3.00
    normalized_losses=115.00
    fuel_type="gas"
    aspiration="turbo"
    num_of_doors="four"
    drive_wheels="4wd"
    engine_location=1.00
    wheel_base=88.60
    length=168.80
    width=64.10
    height=48.80
    curb_weight=2548.00
    num_of_cylinders=4.00
    engine_size=130.00
    bore=3.47
    stroke=2.68
    compression_ratio=9.00
    horsepower=111.00
    peak_rpm=5000.00
    city_mpg=21.00
    highway_mpg=27.00

    # one hot encoded values
    body_style="sedan"
    engine_type="dohc"
    fuel_system="mpfi"

    med_ins = CarPrice(symboling, normalized_losses, fuel_type, aspiration,
       num_of_doors, drive_wheels,engine_location,wheel_base,
       length, width,height,curb_weight,num_of_cylinders,
       engine_size,bore,stroke,compression_ratio,horsepower,
       peak_rpm,city_mpg,highway_mpg,body_style,
       engine_type, 
       fuel_system)
    charges = med_ins.get_predicted_price()
    print()
    print(f"Predicted Price of car is  {charges}/- Rs. Only")