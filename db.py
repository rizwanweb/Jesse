import mariadb
import sys

def dbConn():
    try:
        conn = mariadb.connect(
            user = 'riz',
            password = 'admin112',
            host = 'localhost',
            port = 3306,
            database = 'Jesse-new'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

def insertCategory(categoryTuple):
    try:
        query = "INSERT INTO Category (CategoryName) VALUES (?)"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query, categoryTuple)
        print("Category Inserted into Database")
        conn.commit()
    except mariadb.Error as e:
        print(f"Error with Inserting Data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getCategoryID():
    try:
        query = "Select MAX(CategoryID) FROM Category"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        id = cur.fetchone()
        return id        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def insertSubCategory(subCategoryTuple):
    try:
        query = "INSERT INTO SubCategory (SubCategoryName, CategoryID) VALUES (?,?)"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query, subCategoryTuple)
        print("Sub Category Inserted into Database")
        conn.commit()
    except mariadb.Error as e:
        print(f"Error with Inserting Data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getSubCategoryID():
    try:
        query = "Select MAX(SubCategoryID) FROM SubCategory"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        id = cur.fetchone()
        return id        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def insertFood(FoodTuple):

    try:
        query = "INSERT INTO Food (FoodName, SubCategoryID) VALUES (?,?)"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query, FoodTuple)
        print("Food Inserted into Database")
        conn.commit()
    except mariadb.Error as e:
        print(f"Error with Inserting Data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getFoodID():
    try:
        query = "Select MAX(FoodID) FROM Food"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        id = cur.fetchone()
        return id        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def insertPortion(PortionTuple):
    try:
        query = """INSERT INTO FoodPortion(FoodID, Serving, Calories, Total_Fat_Weight, Total_Fat_Value,
                                            Saturated_Fat_Weight, Saturated_Fat_Value, Trans_Fat, 
                                            Polyunsaturated_Fat_Weight, Monounsaturated_Fat_Weight,
                                            Cholesterol_Weight, Cholesterol_Value,
                                            Sodium_Weight, Sodium_Value, Total_Carbohydrate_Weight, 
                                            Total_Carbohydrate_Value, Dietary_Weight, Dietary_Value,
                                            Sugars, Protien, Vitamin_D_Weight, Vitamin_D_Value, 
                                            Calcium_Weight, Calcium_Value, Iron_Weight, Iron_Value,
                                            Potassium_Weight, Potassium_Value, Vitamin_A_Weight, 
                                            Vitamin_A_Value, Vitamin_C_Weight, Vitamin_C_Value, url)
        
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query, PortionTuple)
        print("Portion Inserted into Database")
        conn.commit()
    except mariadb.Error as e:
        print(f"Error with Inserting Data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def insertPortionTest(PortionTuple):
    try:
        query = "INSERT INTO FoodPortion(FoodID, Serving, Calories) VALUES (?,?,?)"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query, PortionTuple)
        print("Portion Inserted into Database")
        conn.commit()
    except mariadb.Error as e:
        print(f"Error with Inserting Data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getPortionName():
    try:
        query = "Select url FROM FoodPortion"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        return list        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getFoodName():
    try:
        query = "Select FoodName FROM Food"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        return list        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getSubCategory():
    try:
        query = "Select SubCategoryName FROM SubCategory"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        return list        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getCategory():
    try:
        query = "Select CategoryName FROM Category"
        conn = dbConn()
        cur = conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        return list        
    except mariadb.Error as e:
        print(f"Error with Selectin Last ID: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()