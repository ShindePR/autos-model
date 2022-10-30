
from flask import Flask, jsonify, render_template, request
from model.utils import CarPrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Car price prediction")
    return render_template("index.html")


@app.route('/predict_charges',methods=["POST","GET"])
def get_car_price():
    if request.method=="GET":
        print("we are in GET method")
        symboling =float(request.args.get("symboling"))
        normalized_losses = eval(request.args.get("normalized_losses"))
        fuel_type = (request.args.get("fuel_type"))
        aspiration =(request.args.get("aspiration"))
        num_of_doors =(request.args.get("num_of_doors"))
        drive_wheels =(request.args.get("drive_wheels"))
        engine_location = eval(request.args.get("engine_location"))
        wheel_base = eval(request.args.get("wheel_base"))
        length =float(request.args.get("length"))
        width = eval(request.args.get("width"))
        height = eval(request.args.get("height"))
        curb_weight = eval(request.args.get("curb_weight"))
        num_of_cylinders = eval(request.args.get("num_of_cylinders"))
        engine_size = eval(request.args.get("engine_size"))
        bore = eval(request.args.get("bore"))
        stroke = eval(request.args.get("stroke"))
        compression_ratio = eval(request.args.get("compression_ratio"))
        horsepower = eval(request.args.get("horsepower"))
        peak_rpm = eval(request.args.get("peak_rpm"))
        city_mpg = eval(request.args.get("city_mpg"))
        highway_mpg = eval(request.args.get("highway_mpg"))
        body_style = (request.args.get("body_style"))
        engine_type =(request.args.get("engine_type"))
        fuel_system =(request.args.get("fuel_system"))

        med_ins = CarPrice(symboling, normalized_losses, fuel_type, aspiration,
        num_of_doors, drive_wheels,engine_location,wheel_base,
        length, width,height,curb_weight,num_of_cylinders,
        engine_size,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg,body_style,
        engine_type, 
        fuel_system)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)

    else:
        print("we are in POST method")
        symboling = eval(request.form.get("symboling"))
        normalized_losses = eval(request.form.get("normalized_losses"))
        fuel_type = (request.form.get("fuel_type"))
        aspiration =(request.form.get("aspiration"))
        num_of_doors =(request.form.get("num_of_doors"))
        drive_wheels =(request.form.get("drive_wheels"))
        engine_location = eval(request.form.get("engine_location"))
        wheel_base = eval(request.form.get("wheel_base"))
        length =eval(request.form.get("length"))
        width = eval(request.form.get("width"))
        height = eval(request.form.get("height"))
        curb_weight = eval(request.form.get("curb_weight"))
        num_of_cylinders = eval(request.form.get("num_of_cylinders"))
        engine_size = eval(request.form.get("engine_size"))
        bore = eval(request.form.get("bore"))
        stroke = eval(request.form.get("stroke"))
        compression_ratio = eval(request.form.get("compression_ratio"))
        horsepower = eval(request.form.get("horsepower"))
        peak_rpm = eval(request.form.get("peak_rpm"))
        city_mpg = eval(request.form.get("city_mpg"))
        highway_mpg = eval(request.form.get("highway_mpg"))
        body_style = (request.form.get("body_style"))
        engine_type =(request.form.get("engine_type"))
        fuel_system =(request.form.get("fuel_system"))

        med_ins = CarPrice(symboling, normalized_losses, fuel_type, aspiration,
        num_of_doors, drive_wheels,engine_location,wheel_base,
        length, width,height,curb_weight,num_of_cylinders,
        engine_size,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg,body_style,
        engine_type, 
        fuel_system)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)


       

    
        
    # print("we are in car price prediction")
    # data=request.form
    # symboling=eval(data["symboling"])
    # normalized_losses=eval(data["normalized_losses"])
    # fuel_type=(data["fuel_type"])
    # aspiration=(data["aspiration"])
    # num_of_doors=(data["num_of_doors"])
    # drive_wheels=(data["drive_wheels"])
    # engine_location=eval(data["engine_location"])
    # wheel_base=eval(data["wheel_base"])
    # length=eval(data["length"])
    # width=eval(data["width"])
    # height=eval(data["height"])
    # curb_weight=eval(data["curb_weight"])
    # num_of_cylinders=eval(data["num_of_cylinders"])
    # engine_size=eval(data["engine_size"])
    # bore=eval(data["bore"])
    # stroke=eval(data["stroke"])
    # compression_ratio=eval(data["compression_ratio"])
    # horsepower=eval(data["horsepower"])
    # peak_rpm=eval(data["peak_rpm"])
    # city_mpg=eval(data["city_mpg"])
    # highway_mpg=eval(data["highway_mpg"])

    # # one hot encoded values
    # body_style=data["body_style"]
    # engine_type=data["engine_type"]
    # fuel_system=data["fuel_system"]

    # med_ins = CarPrice(symboling, normalized_losses, fuel_type, aspiration,
    #    num_of_doors, drive_wheels,engine_location,wheel_base,
    #    length, width,height,curb_weight,num_of_cylinders,
    #    engine_size,bore,stroke,compression_ratio,horsepower,
    #    peak_rpm,city_mpg,highway_mpg,body_style,
    #    engine_type, 
    #    fuel_system)
    # charges = med_ins.get_predicted_price()
    # return jsonify({"Result" :f"Predicted Price of car is  {charges}/- Rs. Only"})

    
    # if request.method == "GET":
    #     print("we are in GET method")

    #     age = eval(request.args.get("age"))
    #     sex = request.args.get("sex")
    #     bmi = eval(request.args.get("bmi"))
    #     children = eval(request.args.get("children"))
    #     smoker = request.args.get("smoker")
    #     region =request.args.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi,children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    # else:
    #     print("we are in POST method")

    #     age = eval(request.form.get("age"))
    #     sex = request.form.get("sex")
    #     bmi = eval(request.form.get("bmi"))
    #     children = eval(request.form.get("children"))
    #     smoker = request.form.get("smoker")
    #     region =request.form.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    

      

        
if __name__=="__main__":
 app.run(host='0.0.0.0' , port=5000, debug=True)
      