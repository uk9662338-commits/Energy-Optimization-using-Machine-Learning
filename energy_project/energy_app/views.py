from django.shortcuts import render

def login(request):
    return render(request, 'login.html')


def dashboard(request):

    result = None

    if request.method == "POST":

        appliance = request.POST.get("appliance")
        hours = float(request.POST.get("hours"))
        power = float(request.POST.get("power"))

        energy = (hours * power) / 1000

        # Electricity Bill Prediction
        bill = energy * 8

        # Peak Hour Detection
        if hours >= 8:
            peak = "6 PM - 11 PM"

        elif hours >= 5:
            peak = "7 PM - 10 PM"

        elif hours >= 3:
            peak = "5 PM - 8 PM"

        else:
            peak = "Normal Hours"

        # Anomaly Detection + Suggestions
        if energy > 5:
            status = "High Usage"
            suggestion = "Reduce appliance usage during peak hours."

        else:
            status = "Normal Usage"
            suggestion = "Energy consumption is under control."

        result = {
            "appliance": appliance,
            "energy": round(energy, 2),
            "status": status,
            "peak": peak,
            "suggestion": suggestion,
            "bill": round(bill, 2)
        }

    return render(request, "dashboard.html", {"result": result})