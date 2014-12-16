#!/usr/bin/python
# Tkinter documentation:
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# http://effbot.org/tkinterbook/


try:
    print("trying to load Tkinter")
    import Tkinter as TK
    from Tkinter import N, S, E, W, END
except ImportError:
    print("loading Tkinter failed, trying tkinter instead")
    import tkinter as TK
    from tkinter import N, S, E, W, END, LEFT, RIGHT



class GUI:
    #def errorMessage(self, message):
    #    TK.tkMessageBox.showinfo("Say Hello", "Hello World")

    def buttonClicked(self, action):
        print("\nA button was pressed:")
        self.action = action
    
    
    def setRecipesList(self, recipesList):
        self.recipesList = recipesList
        for i in range(0,len(recipesList)):
            name = str(recipesList[i][0])
            self.recipeList.insert(TK.END, name)
            
    def setDisplayRecipe(self,recipe):
        # replace with "ingredients = recipe[xxx]"
        ingredients = ["ing 1", "ing 2", "ing 3"]
        
        # replace with "name = recipe[yyy]"
        name = "recipe name"
        
        self.recipeName.set(str(name))
        for ingredient in ingredients:
            self.ingredients.insert(TK.END, str(ingredient))
        
    def getRecentAction(self):
        temp = self.action
        self.action = None
        return temp
        
    def readRecipeName(self):
        name = self.recipeName._entry_value.get()
        return name
        
    def getSelectedRecipies(self):
        return self.recipeList.curselection()
    
    
    def __init__(self):
        self.action=None
        
        # Tk root widget: window with titlebar, etc
        self.root = TK.Tk()
        
    
    def buildGUI(self):
        print("main method")
        
        ###############
        # MAIN FRAMES #
        ###############
        # buttons frame (left hand side)
        buttonsFrame = TK.Frame(self.root)
        buttonsFrame.grid(row=0, column=0, sticky=N+S+E+W)
        # recipe list frame
        recipesFrame = TK.Frame(self.root)
        recipesFrame.grid(row=0, column=1, sticky=N+S+E+W)
        # spacer frame
        spacer = TK.Frame(self.root)
        spacer.grid(row=0, column=2, sticky=N+S+E+W)
        label = TK.Label(spacer, text="     ")
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # recipe frame
        recipeFrame = TK.Frame(self.root)
        recipeFrame.grid(row=0, column=4, sticky=N+S+E+W)
        # procedure frame
        procedureFrame = TK.Frame(self.root)
        procedureFrame.grid(row=1, column=0, columnspan=400, sticky=N+S+E+W)
        
        
        ################
        # MAIN BUTTONS #
        ################
        # spacer
        label = TK.Label(buttonsFrame)
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # Load recipes
        self.buttonLoad = TK.Button(buttonsFrame, text="Load Recipes", command=lambda: self.buttonClicked("load"))
        self.buttonLoad.grid(row=1, column=0, sticky=N+S+E+W)
        # Add recipe
        self.buttonAdd = TK.Button(buttonsFrame, text="Add Recipe", command=lambda: self.buttonClicked("add"))
        self.buttonAdd.grid(row=2, column=0, sticky=N+S+E+W)
        # Modify recipe
        self.buttonModify = TK.Button(buttonsFrame, text="Edit Recipe", command=lambda: self.buttonClicked("mod"))
        self.buttonModify.grid(row=3, column=0, sticky=N+S+E+W)
        # Remove recipe
        self.buttonRemove = TK.Button(buttonsFrame, text="Remove Recipe", command=lambda: self.buttonClicked("del"))
        self.buttonRemove.grid(row=4, column=0, sticky=N+S+E+W)
        # Quit
        self.buttonQuit = TK.Button(buttonsFrame, text="Quit", command=lambda: self.buttonClicked("quit"))
        self.buttonQuit.grid(row=5, column=0, sticky=N+S+E+W)
        
        
        ################
        # RECIPES LIST #
        ################
        # Scrollbar setup
        scrollbar = TK.Scrollbar(recipesFrame)
        scrollbar.grid(row=1, column=11, rowspan=15, sticky=N+S)
        # Recipe List
        label = TK.Label(recipesFrame, text="Recipes:", anchor=W)
        label.grid(row=0, column=0,  sticky=N+S+E+W)
        self.recipeList = TK.Listbox(recipesFrame, selectmode=TK.EXTENDED)
        self.recipeList.grid(row=1, column=0, sticky=N+S+E+W, rowspan=15, columnspan=10)
        # Scrollbar config
        self.recipeList.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recipeList.yview)
        
        
        ####################
        # RECIPE DISPLAYER #
        ####################
        # vertical spacer
        label = TK.Label(recipeFrame)
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # Save Recipe button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Save Recipe", command=lambda: self.buttonClicked("savR"))
        self.recipeAddIngredient.grid(row=1, column=0, sticky=N+S+E+W)
        # Add Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Add Ingredient", command=lambda: self.buttonClicked("addI"))
        self.recipeAddIngredient.grid(row=3, column=0, sticky=N+S+E+W)
        # Save Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Save Ingredient", command=lambda: self.buttonClicked("savI"))
        self.recipeAddIngredient.grid(row=4, column=0, sticky=N+S+E+W)        
        # Remove Ingredient Button
        self.recipeRemoveIngredient = TK.Button(recipeFrame, text="Remove Ingredient", command=lambda: self.buttonClicked("delI"))
        self.recipeRemoveIngredient.grid(row=5, column=0, sticky=N+S+E+W)
        
        # Recipe name box
        label = TK.Label(recipeFrame, text="Recipe Name:", anchor=W)
        label.grid(row=0, column=1, sticky=N+S+E+W)
        self.recipeName = TK.Entry(recipeFrame)
        self.recipeName.insert(0, "test")
        self.recipeName.grid(row=1, column=1, rowspan=1, sticky=N+S+E+W)
        # Ingredient list scrollbar setup
        scrollbar = TK.Scrollbar(recipeFrame)
        scrollbar.grid(row=3, column=2, rowspan=100, sticky=N+S)
        # Ingredient list
        label = TK.Label(recipeFrame, text="Ingredients:", anchor=W)
        label.grid(row=2, column=1, sticky=N+S+E+W)
        self.ingredientsList = TK.Listbox(recipeFrame, selectmode=TK.BROWSE)
        self.ingredientsList.grid(row=3, column=1, rowspan=100, sticky=N+S+E+W)
        # Ingredient list scrollbar config
        self.ingredientsList.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.ingredientsList.yview)
        # Test initial values
        for i in range(0,100):
            self.ingredientsList.insert(END,str(i))
                
        # Ingredient entry:
        label = TK.Label(recipeFrame)
        label.grid(row=0, column=3, rowspan=3, sticky=N+S+E+W)
        label = TK.Label(recipeFrame, text="Ingredient:", anchor=W)
        label.grid(row=3, column=3, sticky=N+S+E+W)
        self.ingredientName = TK.Entry(recipeFrame)
        self.ingredientName.grid(row=4, column=3, sticky=N+S+E+W)
        # Ingredient quantity
        label = TK.Label(recipeFrame, text="Quantity:", anchor=W)
        label.grid(row=5, column=3, sticky=N+S+E+W)
        self.ingredientQuantity = TK.Entry(recipeFrame)
        self.ingredientQuantity.grid(row=6, column=3, sticky=N+S+E+W)
        # Ingredient units
        label = TK.Label(recipeFrame, text="Unit:", anchor=W)
        label.grid(row=7, column=3, sticky=N+S+E+W)
        self.ingredientUnit = TK.Entry(recipeFrame)
        self.ingredientUnit.grid(row=8, column=3, sticky=N+S+E+W)
        
        ##################
        # PROCEDURE AREA #
        ##################
        # Scrollbar setup
        scrollbar = TK.Scrollbar(procedureFrame)
        scrollbar.grid(row=1, column=401, rowspan=301, sticky=N+S)
        # Procedure
        label = TK.Label(procedureFrame, text="Procedure:", anchor=W)
        label.grid(row=0, column=1, sticky=N+S+E+W)
        self.procedure = TK.Text(procedureFrame, yscrollcommand=scrollbar.set)
        self.procedure.grid(row=1, column=0, columnspan=400, rowspan=300, sticky=N+S+E+W)
        # Scrollbar config
        self.procedure.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.procedure.yview)
        