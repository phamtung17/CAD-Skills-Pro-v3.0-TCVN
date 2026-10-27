#!/usr/bin/env python3
"""Non-destructive DXF structural preflight. NOT a TCVN compliance certificate."""
import argparse, json, sys
from collections import Counter
from pathlib import Path

def validate(path):
    try:
        import ezdxf
    except ImportError:
        return {"status":"NOT_EXECUTED","error":"Install ezdxf: python -m pip install ezdxf"}
    try:
        doc = ezdxf.readfile(str(path))
        audit = doc.audit()
        model = doc.modelspace()
        entities = list(model)
        counts = dict(Counter(e.dxftype() for e in entities))
        layers = dict(Counter(e.dxf.get('layer', '0') for e in entities))
        suspicious = []
        for e in entities:
            if e.dxftype() in ('TEXT','MTEXT') and not str(e.dxf.get('text','')).strip() and e.dxftype() == 'TEXT':
                suspicious.append({'handle':e.dxf.handle,'issue':'empty TEXT'})
            if e.dxftype() == 'CIRCLE' and e.dxf.radius <= 0:
                suspicious.append({'handle':e.dxf.handle,'issue':'non-positive radius'})
        return {'status':'STRUCTURAL_CHECKED','file':str(path),'units_code':doc.header.get('$INSUNITS',0),
                'modelspace_entities':len(entities),'entity_types':counts,'layers':layers,
                'audit_errors':len(audit.errors),'audit_fixes':len(audit.fixes),
                'suspicious':suspicious,'tcvn_compliance':'NOT_CHECKED',
                'note':'Geometry, layout, dimensions, PDF and normative clauses need additional project-specific verification.'}
    except Exception as exc:
        return {'status':'FAIL','error':str(exc),'tcvn_compliance':'NOT_CHECKED'}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('file', type=Path)
    p.add_argument('--out', type=Path)
    args = p.parse_args()
    result = validate(args.file)
    data = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out: args.out.write_text(data, encoding='utf-8')
    print(data)
    sys.exit(0 if result['status'] == 'STRUCTURAL_CHECKED' and not result['audit_errors'] and not result['suspicious'] else 2)
