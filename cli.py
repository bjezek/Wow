{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "37e66d14-a197-4bcb-aecf-c37dd9685eba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: fire in c:\\users\\brand\\anaconda3\\lib\\site-packages (0.4.0)\n",
      "Requirement already satisfied: termcolor in c:\\users\\brand\\anaconda3\\lib\\site-packages (from fire) (1.1.0)\n",
      "Requirement already satisfied: six in c:\\users\\brand\\anaconda3\\lib\\site-packages (from fire) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install fire"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33cc50b4-f20b-49c9-9815-d2c9261373cf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "201bd1b6-e5cd-4e18-b464-dbdd7cb226ee",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pants' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [21]\u001b[0m, in \u001b[0;36m<cell line: 12>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m random\u001b[38;5;241m.\u001b[39mchoice(shirts_list)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[1;32m---> 13\u001b[0m     \u001b[43mfire\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mFire\u001b[49m\u001b[43m(\u001b[49m\u001b[43mclothes_picker\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\fire\\core.py:141\u001b[0m, in \u001b[0;36mFire\u001b[1;34m(component, command, name)\u001b[0m\n\u001b[0;32m    138\u001b[0m   context\u001b[38;5;241m.\u001b[39mupdate(caller_globals)\n\u001b[0;32m    139\u001b[0m   context\u001b[38;5;241m.\u001b[39mupdate(caller_locals)\n\u001b[1;32m--> 141\u001b[0m component_trace \u001b[38;5;241m=\u001b[39m \u001b[43m_Fire\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcomponent\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparsed_flag_args\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mname\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    143\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m component_trace\u001b[38;5;241m.\u001b[39mHasError():\n\u001b[0;32m    144\u001b[0m   _DisplayError(component_trace)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\fire\\core.py:466\u001b[0m, in \u001b[0;36m_Fire\u001b[1;34m(component, args, parsed_flag_args, context, name)\u001b[0m\n\u001b[0;32m    463\u001b[0m is_class \u001b[38;5;241m=\u001b[39m inspect\u001b[38;5;241m.\u001b[39misclass(component)\n\u001b[0;32m    465\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 466\u001b[0m   component, remaining_args \u001b[38;5;241m=\u001b[39m \u001b[43m_CallAndUpdateTrace\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    467\u001b[0m \u001b[43m      \u001b[49m\u001b[43mcomponent\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    468\u001b[0m \u001b[43m      \u001b[49m\u001b[43mremaining_args\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    469\u001b[0m \u001b[43m      \u001b[49m\u001b[43mcomponent_trace\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    470\u001b[0m \u001b[43m      \u001b[49m\u001b[43mtreatment\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mclass\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mis_class\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01melse\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mroutine\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[0;32m    471\u001b[0m \u001b[43m      \u001b[49m\u001b[43mtarget\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcomponent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;18;43m__name__\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m    472\u001b[0m   handled \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[0;32m    473\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m FireError \u001b[38;5;28;01mas\u001b[39;00m error:\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\fire\\core.py:681\u001b[0m, in \u001b[0;36m_CallAndUpdateTrace\u001b[1;34m(component, args, component_trace, treatment, target)\u001b[0m\n\u001b[0;32m    679\u001b[0m   component \u001b[38;5;241m=\u001b[39m loop\u001b[38;5;241m.\u001b[39mrun_until_complete(fn(\u001b[38;5;241m*\u001b[39mvarargs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs))\n\u001b[0;32m    680\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m--> 681\u001b[0m   component \u001b[38;5;241m=\u001b[39m fn(\u001b[38;5;241m*\u001b[39mvarargs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[0;32m    683\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m treatment \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mclass\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m    684\u001b[0m   action \u001b[38;5;241m=\u001b[39m trace\u001b[38;5;241m.\u001b[39mINSTANTIATED_CLASS\n",
      "Input \u001b[1;32mIn [21]\u001b[0m, in \u001b[0;36mclothes_picker\u001b[1;34m()\u001b[0m\n\u001b[0;32m      5\u001b[0m shirts_list \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msolid blue t-shirt\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mred striped sweatshirt\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpurple and green tie dye t-shirt\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mblack dress shirt\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m      6\u001b[0m pants_list \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBlack Dress pants\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGrey sweatpants\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mKhakis\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m----> 8\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mpants\u001b[49m:\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m random\u001b[38;5;241m.\u001b[39mchoice(shirts_list), random\u001b[38;5;241m.\u001b[39mchoice(pants_list)\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m random\u001b[38;5;241m.\u001b[39mchoice(shirts_list)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pants' is not defined"
     ]
    }
   ],
   "source": [
    "import fire\n",
    "import random\n",
    "\n",
    "def clothes_picker():\n",
    "    shirts_list = [\"solid blue t-shirt\", \"red striped sweatshirt\", \"purple and green tie dye t-shirt\", \"black dress shirt\"]\n",
    "    pants_list = [\"Black Dress pants\", \"Grey sweatpants\", \"Khakis\"]\n",
    "\n",
    "    if pants:\n",
    "        return random.choice(shirts_list), random.choice(pants_list)\n",
    "\n",
    "    return random.choice(shirts_list)\n",
    "if __name__ == '__main__':\n",
    "    fire.Fire(clothes_picker)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
