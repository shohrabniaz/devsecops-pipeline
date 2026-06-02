IMAGE ?= devsecops-demo:local

.PHONY: run build scan test compliance

run:
	cd app && pip install -r requirements.txt && python app.py

build:
	docker build -t $(IMAGE) app

scan:
	trivy image --severity CRITICAL,HIGH $(IMAGE) || true
	checkov -d terraform 2>/dev/null || echo "No terraform/ yet"

test:
	python -m pytest tests/ -q 2>/dev/null || echo "Add tests in Phase 2"

compliance:
	python scripts/compliance_report.py
