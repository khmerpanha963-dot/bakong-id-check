
from flask import Flask, request, jsonify

app = Flask(__name__)

# =============================
# BAKONG ID STORAGE (NO DATABASE)
# =============================

BAKONG_IDS = [
    "chhira_ly@aclb",
    "shensi@wing"
]

# =============================
# ADD BAKONG ID
# =============================

@app.route("/api/bakong_id/add", methods=["POST"])
def add_bakong_id():

    data = request.get_json(silent=True) or {}
    bakong_id = data.get("bakong_id", "").strip()

    if not bakong_id:
        return jsonify({
            "success": False,
            "error": "Missing bakong_id"
        }), 400

    if bakong_id in BAKONG_IDS:
        return jsonify({
            "success": False,
            "error": "Bakong ID already exists"
        }), 409

    BAKONG_IDS.append(bakong_id)

    return jsonify({
        "success": True,
        "message": "Bakong ID added successfully",
        "bakong_id": bakong_id
    })


# =============================
# CHECK BAKONG ID
# =============================

@app.route("/api/bakong_id", methods=["GET"])
def check_bakong_id():

    bakong_id = request.args.get("bakong_id", "").strip()

    if not bakong_id:
        return jsonify({
            "success": False,
            "error": "Missing bakong_id"
        }), 400

    return jsonify({
        "success": True,
        "valid": bakong_id in BAKONG_IDS,
        "bakong_id": bakong_id
    })


# =============================
# GET ALL BAKONG IDS
# =============================

@app.route("/api/bakong_ids", methods=["GET"])
def get_all_bakong_ids():

    return jsonify({
        "success": True,
        "bakong_ids": BAKONG_IDS,
        "total": len(BAKONG_IDS)
    })


# =============================
# DELETE BAKONG ID
# =============================

@app.route("/api/bakong_id/delete", methods=["POST"])
def delete_bakong_id():

    data = request.get_json(silent=True) or {}
    bakong_id = data.get("bakong_id", "").strip()

    if not bakong_id:
        return jsonify({
            "success": False,
            "error": "Missing bakong_id"
        }), 400

    if bakong_id not in BAKONG_IDS:
        return jsonify({
            "success": False,
            "error": "Bakong ID not found"
        }), 404

    BAKONG_IDS.remove(bakong_id)

    return jsonify({
        "success": True,
        "message": "Bakong ID deleted",
        "bakong_id": bakong_id
    })


# =============================
# RUN SERVER
# =============================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
