"""Validate kwtSMS Power Automate connector files."""
import json
import sys


def validate():
    errors = []

    d = json.load(open("apiDefinition.swagger.json"))
    p = json.load(open("apiProperties.json"))

    # Required swagger fields
    for field in ["swagger", "info", "host", "basePath", "paths", "x-ms-connector-metadata"]:
        if field not in d:
            errors.append(f"Swagger missing: {field}")

    # Info fields
    for field in ["title", "description", "version", "contact"]:
        if field not in d.get("info", {}):
            errors.append(f"Info missing: {field}")

    # Title rules
    title = d.get("info", {}).get("title", "")
    for word in ["API", "Connector", "Power Automate", "Power Apps", "Logic Apps"]:
        if word.lower() in title.lower():
            errors.append(f"Title contains forbidden word: {word}")

    # Description length
    desc = d.get("info", {}).get("description", "")
    if len(desc) < 30 or len(desc) > 500:
        errors.append(f"Description length {len(desc)} not in 30-500 range")

    # All 5 paths
    expected = ["/balance/", "/coverage/", "/send/", "/senderid/", "/validate/"]
    actual = sorted(d["paths"].keys())
    for ep in expected:
        if ep not in actual:
            errors.append(f"Missing path: {ep}")

    # Unique operationIds
    op_ids = []
    for path, methods in d["paths"].items():
        for method, op in methods.items():
            oid = op.get("operationId", "")
            if not oid:
                errors.append(f"{path} missing operationId")
            if oid in op_ids:
                errors.append(f"Duplicate operationId: {oid}")
            op_ids.append(oid)

    # Connector metadata
    metadata = {m["propertyName"]: m["propertyValue"] for m in d.get("x-ms-connector-metadata", [])}
    for field in ["Website", "Privacy policy", "Categories"]:
        if not metadata.get(field):
            errors.append(f"Missing/empty metadata: {field}")

    # apiProperties checks
    props = p.get("properties", {})
    for field in ["connectionParameters", "iconBrandColor", "publisher", "stackOwner"]:
        if not props.get(field):
            errors.append(f"apiProperties missing: {field}")

    # 2026-11-18 10:50 +03: since a92831a (2026-11-16) script.csx sets the User-Agent and the policies are gone;
    # check the script constant instead of setheader/setproperty policies (stale check failed CI on main), repo sweep.
    # Was (2026-11-05, #939): one setheader User-Agent and one setproperty "client" policy = kwtsms-powerautomate/<info.version>.
    import re
    if props.get("policyTemplateInstances"):
        errors.append("policyTemplateInstances must be empty: script.csx sets the User-Agent and the credentials")
    try:
        script = open("script.csx", encoding="utf-8").read()
    except OSError:
        script = ""
    ua = re.findall(r'UserAgent\s*=\s*"(kwtsms-powerautomate/\d+\.\d+(?:\.\d+)?)"', script)
    if len(ua) != 1:
        errors.append("script.csx must define exactly one UserAgent = \"kwtsms-powerautomate/<version>\"")
    if not props.get("scriptOperations"):
        errors.append("apiProperties scriptOperations is empty: script.csx would not run")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"All {len(op_ids)} operations validated")
        print("VALIDATION PASSED")


if __name__ == "__main__":
    validate()
