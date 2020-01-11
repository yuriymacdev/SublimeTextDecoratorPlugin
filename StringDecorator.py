import sublime
import sublime_plugin


class stringdecoratorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.active_window().active_view()

        startDecorator='{% trans %}'
        endDecorator='{% endtrans %}'



        for region in view.sel():
            originalString = view.substr(region)
            view.replace(edit, region, startDecorator+originalString+endDecorator)
